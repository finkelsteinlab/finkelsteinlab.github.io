---
title: 'Claude vs Printer Android Bridge'
date: 2026-08-28
description: 'Rescuing an old Brother laser printer so it can print from Android phones, with Claude Code doing the heavy lifting.'
tags:
  - 'llm'
  - 'hardware'
---

Wednesdays are quickly becoming "burn through my weekly tokens" day.

This Wednesday, I decided to rescue our old HL-4570CDW laser printer. The printer is a tank! It will probably outlast me! The problem is that its too old to pair with our cell phones.

<div class="figures">

<figure>
<img src="/assets/images/blog/claude-vs-printer-android-bridge/printer.jpg" />
<figcaption>Figure 1a. The Brother HL-4570CDW, circa 2010.</figcaption>
</figure>

<figure>
<img src="/assets/images/blog/claude-vs-printer-android-bridge/tank.jpg" />
<figcaption>Figure 1b. An M1A1 Abrams, for comparison. Photo: Tech. Sgt. John Houghton, U.S. Air Force (public domain).</figcaption>
</figure>

</div>

The good news is that the **W** in **HL-4570CDW** stands for wireless. The bad news is that it doesn't connect to any modern Android phones.

And my wife has been asking me for the better part of five years now to be able to print documents from her phone directly to the printer.

All I knew was that the printer showed up via [CUPS](https://en.wikipedia.org/wiki/CUPS) on our home network with a static IP. And I told Fable what I wanted:

    draft an md plan file then launch a fable agent to inspect and critique.

Claudish … Claudish … Claudish…

The critique found three design errors before a line of code existed. They became corrections, not debugging sessions.

    do all of them, work independently until u finish

After "gibbering" for about an hour, Fable gave me three choices that were all beyond my comprehension.

I went with what sounded like a standalone app I could sideload via "USB Debugging" on our phones. Sadly, Google is making this route more difficult [in 2027](https://www.androidauthority.com/android-sideloading-changes-timeline-3679204/).

Fable spit out this code: [ifinkelstein/printer-android-bridge](https://github.com/ifinkelstein/printer-android-bridge).

Lo and behold, it installed! And we were off to the printing races!

Good ol' HL-4570CDW is now discoverable on our phones. I'm still amazed that (1) the LLM zero-shotted (zero-shat?) a solution; (2) we could extend this aging, but perfectly capable printer; and (3) I have zero knowledge about Android development. Seems like a great use-case for LLMs!

And I somehow still had plenty of tokens left to burn on other projects (more on that later).

Now I keep thinking that there's so much more old equipment that we can rescue from the garbage heap with our new LLM capabilities.

Most importantly: happy wife, happy life.

PS. This post was inspired by a few other blogs that rescued old hardware via similar means:

- [Raiders of the Lost Array](https://fetzu.ch/blog/20260819_claudevsdrobo/): a macOS driver and companion app for an orphaned Drobo 5D storage array. Claude reverse-engineered the proprietary protocol from the defunct manufacturer's binaries. ([HN](https://news.ycombinator.com/item?id=49368911))
- [A macOS driver for the Windows-only HP Laser 1008a](https://github.com/Kuberwastaken/hp-laser-1008a-macos): Kuber Mehta had Claude Code patch the open-source SpliX driver to speak the printer's SPL3 raster language, so Cmd-P just works. ([HN](https://news.ycombinator.com/item?id=49344643))
- [Using Claude Code to modernize a 25-year-old kernel driver](https://dmitrybrant.com/2025/09/07/using-claude-code-to-modernize-a-25-year-old-kernel-driver): Dmitry Brant ported the `ftape` floppy-controller tape driver to Linux 6.8 to recover data from QIC-80 cartridges. ([HN](https://news.ycombinator.com/item?id=45163362))
