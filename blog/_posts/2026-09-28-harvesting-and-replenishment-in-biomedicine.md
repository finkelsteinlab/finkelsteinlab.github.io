---
title: 'Harvesting and Replenishment in Biomedicine'
date: 2026-09-28
description: 'Anthropic''s agents found an interesting enzyme system in a public database, or maybe not.'
tags:
  - 'ai'
  - 'crispr'
  - 'genomics'
---

Since I work on CRISPR and retrons–bacterial defense systems with a reverse transcriptase (RT)–several people sent me Anthropic's big announcement. Their claim is that Claude "discovered" new RT enzymes with properties that are reminiscent of CRISPR.[^1] This, according to the press release, is "a new way of doing biology research."

So is this a BFD? I've been thinking about it all weekend!

TL;DR: This is an interesting result! If a student brought me this observation, I'd happily pursue it further. But boy-oh-boy, is the hype getting ahead of the actual science.

## An interesting system with unknown significance

A reverse transcriptase (RT) copies RNA into DNA. Famously, many human viruses (e.g., HIV) rely on these types of enzymes. Bacteria have their own RTs, including those in defensive systems that provide primitive immunity against viral infections. These RTs have been a very productive research area[^2][^3][^4][^5][^6][^7]. We, and others, have been developing these RTs into precise genome editors[^8][^9][^10][^11].

So it's perhaps not too surprising that Yoon and colleagues, most of whom are experts in this broad research area, decided to further probe the wild wild west of bacterial RTs. They observed that a class of RTs have an unusual RNA component that's vaguely reminiscent of the CRISPR systems. Most RTs have a nearby non-coding RNA; their systems have an array of three to twenty-one repeats separated by unique spacers (thus the aptly named array-associated reverse transcriptases, or ARTs).[^12]

That arrangement resembles CRISPR, but it's not! The spacers are four to seven times longer, and there are no nearby *cas* genes. Is this the next frontier in therapeutic gene editing? We shall see… there's a very, very long road to answering this question.

> The L0050 (228,907 bp logan contig) flank is spectacular: I can see by eye a **tandem repeat array**: "CATGTGTATCGCATGTT" / "CATGTGTTTCGCATGT" repeating many times with ~100-180 bp spacers — that's a CRISPR-like or msDNA-like repeat array?!
>
> — Worker agent, task t0062[^13]

I have seen people say that any graduate student could have done this. I've supervised students who have done similar projects. In my experience, a junior student could spend a year or more running this type of campaign. And there's no guarantee that they'd see this signal. I am not even sure that a standard DNA repeat finder (e.g., PILER-CR[^14] or other repeat finders) would catch these long spacers and imperfect repeats.

Perhaps most importantly, automating this kind of grunt work accelerates hypothesis generation. With sufficient resources, I'd be doing hundreds of similar campaigns right now. I'm sure Anthropic already is.

## We still need experts

Dr. [Peter Yoon](https://www.linkedin.com/in/peter-hyungjun-yoon) is a Doudna lab alum, and worked on mining CRISPR-Cas13 sequences[^15]. The rest of the team worked on CRISPR (Dr. [Januka Athukoralage](https://www.linkedin.com/in/januka-athukoralage)[^16]) and recombinases (Drs. [Perry](https://www.linkedin.com/in/nicholas-perry-5a6776a3) and [Durrant](https://www.linkedin.com/in/matthew-durrant)). Four of six authors are senior molecular biologists and domain experts. Give that group a heap of compute and frontier models (without safeguards, I'm guessing), and I'm sure we'll be seeing more interesting bioinformatic discoveries. Also, how many "rejected" campaigns are we NOT seeing?

If nothing else, this proves that LLMs are great accelerators for expert-driven hypothesis generation.

## Et tu, Brute?

The *New York Times* reports that a Copenhagen group had been studying something matching this finding and discussing it with Claude.[^17] Similar questions arose over OpenAI's claimed Navier–Stokes breakthrough: had unpublished work by Tristan Buckmaster and Levent Alpöge influenced the result?[^18]

This is a serious allegation, indeed. Many labs are searching the same public databases using the same tools and, indeed, similar LLMs. Is this why Anthropic released such an early result? At the very least, I'd love to see the Anthropic team run a proper, transparent investigation.

So what does this mean for biology in the age of LLMs?

## Harvesting and Replenishment

> We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run.
>
> — Roy Amara ([Amara's law](https://en.wikipedia.org/wiki/Roy_Amara#Amara's_law))

Terence Tao has written extensively on LLM-led Lean proofs in mathematics. He welcomes automated searches that resolve tractable problems in the Erdős database: they get useful work done and surface "harder questions."[^19][^20]

His concern is what the LLM-driven solution leaves behind, and what is lost. Tao argues that human-led "failed approaches" teach us as much as the final proof. An inscrutable, machine-generated solution adds little to mathematics, while discouraging humans from pursuing these problems.[^21][^22]

Biology is, of course, very different. A cure that teaches us very little is still a cure, and I doubt the patients will object. But we also need to keep producing questions, data, and people who can make sense of it all.

Consider the student whose year of bioinformatics training we no longer need. Some of that year is wasted on tedious work. Some is spent learning to recognize a strange locus and deciding whether it deserves another experiment. Did we automate an important training pillar? We do not yet know how trainees will adjust.

And what happens after the big-compute labs strip-mine useful nuggets using public data and open-source tools? When data is gold, will colleagues who do environmental sequencing and bioprospecting be less willing to release their data? Will collaborations freeze? If someone with more compute can strip-mine your dataset in an afternoon, you have every reason to delay that deposit. Mathematicians are already grappling with these very questions.[^23]

That is what I mean by harvesting and replenishment. Of course, we should accelerate new findings by mining public data, ART included! Both the NIH and NSF have long-standing programs aimed at standardizing public datasets for just such research[^24][^25].

But I also want the next big databases to be publically released, the next students trained, and human intuition-driven questions given enough resources to surprise us.

## Back to the bench

Feng Zhang calls ART-RTs "genuinely intriguing" and says they merit "further investigation."[^26] This is indeed an interesting observation.

Now comes the unglamorous, slow work of understanding how ART RTs work, possibly in anti-viral defense, and maybe even as biotechnology tools. This requires many, many experiments. The roadmap for such experiments has already been established by the many research groups that have worked on RTs in the past.

Here, too, Anthropic hopes to make inroads with automated, LLM-driven wet-bench robotics:

> MHS also helps researchers and engineers more readily orchestrate autonomous, round-the-clock experiments and workflows…
>
> — Anthropic, announcing its Model Hardware Standard[^27]

If they succeed here, it will be a much bigger deal than their ART-RT press release.

## Notes

[^1]: Anthropic, "Claude discovers a novel enzyme system," [anthropic.com/news/claude-discovers-novel-enzyme-system](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system), accessed 2026-09-28. Local copy `sources/anthropic-press-release-2026-09-25.html`.

[^2]: Millman A et al. "Bacterial retrons function in anti-phage defense." *Cell* 183, 1551-1561 (2020). [<PMID:33157039>](https://pubmed.ncbi.nlm.nih.gov/33157039/); [<doi:10.1016/j.cell.2020.09.065>](https://doi.org/10.1016/j.cell.2020.09.065).

[^3]: Bobonis J et al. "Bacterial retrons encode phage-defending tripartite toxin-antitoxin systems." *Nature* 609, 144-150 (2022). [<PMID:35850148>](https://pubmed.ncbi.nlm.nih.gov/35850148/); [<doi:10.1038/s41586-022-05091-4>](https://doi.org/10.1038/s41586-022-05091-4).

[^4]: Tang S et al. "De novo gene synthesis by an antiviral reverse transcriptase." *Science* 386, eadq0876 (2024). [<PMID:39116258>](https://pubmed.ncbi.nlm.nih.gov/39116258/); [<doi:10.1126/science.adq0876>](https://doi.org/10.1126/science.adq0876).

[^5]: Song XY et al. "Bacterial reverse transcriptase synthesizes long poly(A)-rich cDNA for antiphage defense." *Science* 388, eads4639 (2025). [<PMID:40310939>](https://pubmed.ncbi.nlm.nih.gov/40310939/); [<doi:10.1126/science.ads4639>](https://doi.org/10.1126/science.ads4639).

[^6]: Carabias A et al. "Retron-Eco1 assembles NAD+-hydrolyzing filaments that provide immunity against bacteriophages." *Molecular Cell* 84, 2185-2202 (2024). [<PMID:38788717>](https://pubmed.ncbi.nlm.nih.gov/38788717/); [<doi:10.1016/j.molcel.2024.05.001>](https://doi.org/10.1016/j.molcel.2024.05.001).

[^7]: Buffington JD et al. "Discovery and engineering of retrons for precise genome editing." *Nature Biotechnology* (2025). [<PMID:41131151>](https://pubmed.ncbi.nlm.nih.gov/41131151/); [<doi:10.1038/s41587-025-02879-3>](https://doi.org/10.1038/s41587-025-02879-3).

[^8]: Buffington JD et al. "Discovery and engineering of retrons for precise genome editing." *Nature Biotechnology* (2025). [<PMID:41131151>](https://pubmed.ncbi.nlm.nih.gov/41131151/); [<doi:10.1038/s41587-025-02879-3>](https://doi.org/10.1038/s41587-025-02879-3).

[^9]: Kong X et al. "Precise genome editing without exogenous donor DNA via retron editing system in human cells." *Protein & Cell* 12, 899-902 (2021). [<PMID:34403072>](https://pubmed.ncbi.nlm.nih.gov/34403072/); [<doi:10.1007/s13238-021-00862-7>](https://doi.org/10.1007/s13238-021-00862-7).

[^10]: Lopez SC, Crawford KD, Lear SK, Bhattarai-Kline S, Shipman SL. "Precise genome editing across kingdoms of life using retron-derived DNA." *Nature Chemical Biology* 18, 199-206 (2022). [<PMID:34949838>](https://pubmed.ncbi.nlm.nih.gov/34949838/); [<doi:10.1038/s41589-021-00927-y>](https://doi.org/10.1038/s41589-021-00927-y).

[^11]: Zhao B, Chen SA, Lee J, Fraser HB. "Bacterial retrons enable precise gene editing in human cells." *The CRISPR Journal* 5, 31-39 (2022). [<PMID:35076284>](https://pubmed.ncbi.nlm.nih.gov/35076284/); [<doi:10.1089/crispr.2021.0065>](https://doi.org/10.1089/crispr.2021.0065).

[^12]: Yoon PH, Athukoralage JS, Ameisen E, Kauderer-Abrams E, Perry NT, Durrant MG. "Autonomous AI agents discover reverse transcriptases with tandem repeat arrays." Preprint, posted 2026-09-23: [www-cdn.anthropic.com/22573675…pdf](https://www-cdn.anthropic.com/22573675ada52a8ca8a97a1a4b4326b2f208a071.pdf). No DOI. Local copy `sources/yoon-et-al-2026-art-preprint.pdf` (md5 `71916c2f91370fd5d9b68a7e21e68bcb`), retrieved 2026-09-28.

[^13]: Yoon et al. (2026), Fig. 1E and accompanying text, quoting worker agent task t0062. Local copy `sources/yoon-et-al-2026-art-preprint.pdf`, retrieved 2026-09-28.

[^14]: Edgar RC. "PILER-CR: fast and accurate identification of CRISPR repeats." *BMC Bioinformatics* (2007). [<PMID:17239253>](https://pubmed.ncbi.nlm.nih.gov/17239253/); [<doi:10.1186/1471-2105-8-18>](https://doi.org/10.1186/1471-2105-8-18).

[^15]: Yoon PH et al. "Structure-guided discovery of ancestral CRISPR-Cas13 ribonucleases." *Science* 385, 538–543 (2024). [<doi:10.1126/science.adq0553>](https://doi.org/10.1126/science.adq0553).

[^16]: Athukoralage JS et al. "An anti-CRISPR viral ring nuclease subverts type III CRISPR immunity." *Nature* 577, 572–575 (2020). [<doi:10.1038/s41586-019-1909-5>](https://doi.org/10.1038/s41586-019-1909-5).

[^17]: Carl Zimmer, "Did Anthropic's A.I. Really Make a Scientific Discovery on Its Own?", *New York Times*, 27 September 2026: [nytimes.com/2026/09/27/science/anthropic-biology-enzyme-mestre.html](https://www.nytimes.com/2026/09/27/science/anthropic-biology-enzyme-mestre.html), accessed 2026-09-28.

[^18]: Davide Castelvecchi, "Who gets credit in the AI era? OpenAI maths bombshell sparks debate," *Nature*, 17 September 2026: [article](https://www.nature.com/articles/d41586-026-02910-w). Joseph Howlett, "OpenAI claims blockbuster math breakthrough amid swirl of controversy," *Scientific American*, 8 September 2026: [article](https://www.scientificamerican.com/article/openai-claims-blockbuster-math-breakthrough-amid-swirl-of-controversy/). Both accessed 2026-09-28.

[^19]: Terence Tao, Mathstodon, 30 November 2025, post 2 of 3: [mathstodon.xyz/@tao/115639984077620023](https://mathstodon.xyz/@tao/115639984077620023), accessed 2026-09-28.

[^20]: Terence Tao, Mathstodon, 30 November 2025, post 3 of 3: [mathstodon.xyz/@tao/115639985263560286](https://mathstodon.xyz/@tao/115639985263560286), accessed 2026-09-28.

[^21]: Terence Tao, Mathstodon, 3 September 2026, post 5 of 6: [mathstodon.xyz/@tao/117207855800042681](https://mathstodon.xyz/@tao/117207855800042681), accessed 2026-09-28.

[^22]: Terence Tao, Mathstodon, 3 September 2026, post 6 of 6: [mathstodon.xyz/@tao/117207856734787448](https://mathstodon.xyz/@tao/117207856734787448), accessed 2026-09-28.

[^23]: Terence Tao, Mathstodon, 8 September 2026, post 3 of 4: [mathstodon.xyz/@tao/117237322160500501](https://mathstodon.xyz/@tao/117237322160500501), accessed 2026-09-28.

[^24]: NIH Common Fund, Big Data to Knowledge (2013-2020): [commonfund.nih.gov/bd2k](https://commonfund.nih.gov/bd2k). NIH Common Fund Data Ecosystem: [commonfund.nih.gov/dataecosystem](https://commonfund.nih.gov/dataecosystem). NIH Bridge2AI: [commonfund.nih.gov/bridge2ai](https://commonfund.nih.gov/bridge2ai). NIH Data Management and Sharing policy, NOT-OD-21-013: [grants.nih.gov/grants/guide/notice-files/NOT-OD-21-013.html](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-21-013.html). All accessed 2026-09-28.

[^25]: NSF, Advances in Biological Informatics, solicitation NSF 12-567: [nsf.gov/funding/opportunities/capacity-infrastructure-capacity-biological-research/nsf12-567/solicitation](https://www.nsf.gov/funding/opportunities/capacity-infrastructure-capacity-biological-research/nsf12-567/solicitation). NSF, Infrastructure Innovation for Biological Research: [nsf.gov/funding/opportunities/innovation-innovative-infrastructure-biological-research](https://www.nsf.gov/funding/opportunities/innovation-innovative-infrastructure-biological-research). Both accessed 2026-09-28.

[^26]: Feng Zhang, quoted in Anthropic, "Claude discovers a novel enzyme system," [anthropic.com/news/claude-discovers-novel-enzyme-system](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system), accessed 2026-09-28. The same sentence is reused in Robert Langreth, "Anthropic Crispr-Like Findings Draw Caution From Scientists," *Bloomberg*, 25 September 2026.

[^27]: Anthropic, "Previewing the Model Hardware Standard," 27 August 2026: [announcement](https://www.anthropic.com/news/model-hardware-standard-research-preview), accessed 2026-09-28.
