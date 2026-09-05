"""Mine Claude Code transcripts: sessions, user-visible tokens, concurrency.
Writes sessions.csv and prompts.csv into ../data."""
import json, glob, os, csv, sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
SINCE = datetime(2026, 6, 4, tzinfo=timezone.utc)
TZ = ZoneInfo("America/Chicago")
PREVIEW = 3           # lines of a tool result the terminal shows collapsed
CPT = 4               # chars per token, rough

def text_of(c):
    if isinstance(c, str): return c
    if isinstance(c, list):
        return "\n".join(x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text")
    return ""

sessions, prompts = [], []
for f in glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl")):
    if datetime.fromtimestamp(os.path.getmtime(f), timezone.utc) < SINCE: continue
    s = dict(session=os.path.basename(f)[:-6], project="", start=None, end=None, n_prompts=0,
             n_tools=0, vis_prose=0, vis_toolhdr=0, vis_preview=0, typed=0,
             hid_think=0, hid_toolinput=0, hid_result=0, hid_notif=0, out_tokens=0, model="")
    seen_msg = set()
    for line in open(f, errors="ignore"):
        try: d = json.loads(line)
        except Exception: continue
        if d.get("isSidechain"): continue
        ts = d.get("timestamp")
        if ts:
            t = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            s["start"] = t if s["start"] is None or t < s["start"] else s["start"]
            s["end"] = t if s["end"] is None or t > s["end"] else s["end"]
        if d.get("cwd") and not s["project"]: s["project"] = os.path.basename(d["cwd"])
        m = d.get("message", {}); c = m.get("content") if isinstance(m, dict) else None
        if d.get("type") == "user":
            human = d.get("promptSource") == "typed" or (d.get("origin") or {}).get("kind") == "human"
            txt = text_of(c)
            if human and txt and not txt.lstrip().startswith("<"):
                s["n_prompts"] += 1; s["typed"] += len(txt)
                prompts.append((s["session"], t.astimezone(TZ).isoformat()))
            elif txt.lstrip().startswith("<"):
                s["hid_notif"] += len(txt)
            if isinstance(c, list):
                for b in c:
                    if isinstance(b, dict) and b.get("type") == "tool_result":
                        r = text_of(b.get("content")); lines = r.splitlines()
                        p = "\n".join(lines[:PREVIEW]); s["vis_preview"] += len(p); s["hid_result"] += len(r) - len(p)
        elif d.get("type") == "assistant":
            if m.get("id") and m["id"] not in seen_msg:
                seen_msg.add(m["id"]); s["out_tokens"] += (m.get("usage") or {}).get("output_tokens", 0)
                s["model"] = m.get("model", s["model"])
            if isinstance(c, list):
                for b in c:
                    t_ = b.get("type")
                    if t_ == "text": s["vis_prose"] += len(b.get("text", ""))
                    elif t_ == "thinking": s["hid_think"] += len(b.get("thinking", ""))
                    elif t_ == "tool_use":
                        s["n_tools"] += 1; inp = b.get("input", {}) or {}
                        s["vis_toolhdr"] += len(b.get("name", "")) + len(str(inp.get("description") or inp.get("file_path") or inp.get("command") or "")[:120])
                        s["hid_toolinput"] += len(json.dumps(inp))
    if s["start"] is None or s["n_prompts"] == 0: continue
    s["start"] = s["start"].astimezone(TZ).isoformat(); s["end"] = s["end"].astimezone(TZ).isoformat()
    s["vis_tokens"] = (s["vis_prose"] + s["vis_toolhdr"] + s["vis_preview"]) // CPT
    s["hid_tokens"] = (s["hid_think"] + s["hid_toolinput"] + s["hid_result"] + s["hid_notif"]) // CPT
    sessions.append(s)


# ---- Codex (~/.codex/sessions), main threads only (subagent/guardian threads are not shown to me)
for f in glob.glob(os.path.expanduser("~/.codex/sessions/*/*/*/*.jsonl")):
    if datetime.fromtimestamp(os.path.getmtime(f), timezone.utc) < SINCE: continue
    try: meta = json.loads(open(f, errors="ignore").readline())
    except Exception: continue
    mp = meta.get("payload", {}) if meta.get("type") == "session_meta" else {}
    if mp.get("source") != "cli": continue
    s = dict(session="codex-" + mp.get("id", os.path.basename(f))[:12], project=os.path.basename(mp.get("cwd", "")),
             start=None, end=None, n_prompts=0, n_tools=0, vis_prose=0, vis_toolhdr=0, vis_preview=0, typed=0,
             hid_think=0, hid_toolinput=0, hid_result=0, hid_notif=0, out_tokens=0, model="codex")
    seen_prompt = set()
    for line in open(f, errors="ignore"):
        try: d = json.loads(line)
        except Exception: continue
        ts = d.get("timestamp")
        if not ts: continue
        t = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        s["start"] = t if s["start"] is None or t < s["start"] else s["start"]
        s["end"] = t if s["end"] is None or t > s["end"] else s["end"]
        typ = d.get("type"); pl = d.get("payload", {}) if isinstance(d.get("payload"), dict) else {}
        pt = pl.get("type")
        is_um = typ == "event_msg" and pt == "user_message"
        is_ic = typ == "event_msg" and pt == "item_completed" and (pl.get("item") or {}).get("type") == "UserMessage"
        if is_um or is_ic:
            item = pl.get("item") or {}
            key = item.get("id") or pl.get("message")
            if key in seen_prompt: continue
            seen_prompt.add(key)
            txt = pl.get("message") or text_of(item.get("content")) or ""
            s["n_prompts"] += 1; s["typed"] += len(txt)
            prompts.append((s["session"], t.astimezone(TZ).isoformat()))
        elif typ == "event_msg" and pt == "token_count":
            tu = (pl.get("info") or {}).get("total_token_usage") or {}
            s["out_tokens"] = max(s["out_tokens"], tu.get("output_tokens", 0))
            s["hid_think"] = max(s["hid_think"], tu.get("reasoning_output_tokens", 0) * CPT)
        elif typ == "response_item":
            if pt == "message" and pl.get("role") == "assistant":
                s["vis_prose"] += sum(len(x.get("text", "")) for x in pl.get("content", []) if isinstance(x, dict))
            elif pt in ("custom_tool_call", "function_call"):
                s["n_tools"] += 1
                inp = pl.get("input") if pt == "custom_tool_call" else pl.get("arguments", "")
                inp = inp if isinstance(inp, str) else json.dumps(inp)
                s["vis_toolhdr"] += len(pl.get("name", "")) + len(inp[:120]); s["hid_toolinput"] += len(inp)
            elif pt in ("custom_tool_call_output", "function_call_output"):
                out = pl.get("output"); r = out if isinstance(out, str) else text_of(out)
                lines = r.splitlines(); pv = "\n".join(lines[:PREVIEW])
                s["vis_preview"] += len(pv); s["hid_result"] += len(r) - len(pv)
            elif pt == "message" and pl.get("role") == "developer":
                s["hid_notif"] += sum(len(x.get("text", "")) for x in pl.get("content", []) if isinstance(x, dict))
    if s["start"] is None or s["n_prompts"] == 0: continue
    s["start"] = s["start"].astimezone(TZ).isoformat(); s["end"] = s["end"].astimezone(TZ).isoformat()
    s["vis_tokens"] = (s["vis_prose"] + s["vis_toolhdr"] + s["vis_preview"]) // CPT
    s["hid_tokens"] = (s["hid_think"] + s["hid_toolinput"] + s["hid_result"] + s["hid_notif"]) // CPT
    sessions.append(s)

sessions.sort(key=lambda s: s["start"])
with open(os.path.join(DATA, "sessions.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(sessions[0].keys())); w.writeheader(); w.writerows(sessions)
with open(os.path.join(DATA, "prompts.csv"), "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["session", "ts"]); w.writerows(prompts)
print(len(sessions), "sessions,", len(prompts), "human prompts;", sum(1 for x in sessions if x["model"]=="codex"), "codex")
