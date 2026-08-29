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

\<two figures, side by side. fig1a: this printer, fig 1b: a tank\>

The good news is that the **W** in **HL-4570CDW** stands for wireless. The bad news is that it doesn't connect to any modern Android phones.

And my wife has been asking me for the better part of five years now to be able to print documents from her phone directly to the printer.

All I knew was that the printer showed up via CUPS on our home network with a static IP. And I told Fable what I wanted:

\<insert prompt here\>

After churning for about an hour, Fable gave me three choices that were all beyond my comprehension.

I went with what sounded like a standalone app I could sideload it via "USB Debugging" on our phones. Sadly, it sounds like Google may be closing this route in coming Android versions: \<find information on when sideloading will be depreciated\>.

Some time later, Fable spit out this code: \< link to a GitHub repo. \>

Lo and behold, it installed! And we were off to the printing races!

Good ol' HL-4570CDW is now discoverable on our phones. I'm still amazed that (1) the LLM zero-shotted a solution; (2) we could extend this aging, but perfectly capable printer; and (3) I have zero knowledge about Android development. Seems like a great use-case for LLMs!

And now I keep thinking that there's so much more old equipment that we can rescue from the garbage heap with our new LLM capabilities.

Most importantly: Happy wife, Happy life.

PS. This post was inspired by a few other blogs that rescued old hardware via similar means:

- [Raiders of the Lost Array](https://fetzu.ch/blog/20260819_claudevsdrobo/): a macOS driver and companion app for an orphaned Drobo 5D storage array. Claude reverse-engineered the proprietary protocol from the defunct manufacturer's binaries. ([HN](https://news.ycombinator.com/item?id=49368911))
- [A macOS driver for the Windows-only HP Laser 1008a](https://github.com/Kuberwastaken/hp-laser-1008a-macos): Kuber Mehta had Claude Code patch the open-source SpliX driver to speak the printer's SPL3 raster language, so Cmd-P just works. ([HN](https://news.ycombinator.com/item?id=49344643), [The Register](https://www.theregister.com/ai-and-ml/2026/08/19/dev-taps-claude-code-to-craft-custom-printer-driver-for-macos/5289875))
- [Using Claude Code to modernize a 25-year-old kernel driver](https://dmitrybrant.com/2025/09/07/using-claude-code-to-modernize-a-25-year-old-kernel-driver): Dmitry Brant ported the `ftape` floppy-controller tape driver to Linux 6.8 to recover data from QIC-80 cartridges. ([HN](https://news.ycombinator.com/item?id=45163362))

The Register's Rupert Goodwins calls this [digital archaeology](https://www.theregister.com/columnists/2026/08/03/claude-code-is-revolutionizing-digital-archaeology-enterprise-better-dig-it/5281676), and cites Claude Code annotating 1980-era Acorn Econet code and designing a Transputer accelerator for an Archimedes. My printer is a much humbler dig, but the same idea.
