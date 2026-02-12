---
title: "Thoughts on CRISPR Delivery Methods"
date: 2026-02-11
description: "A brief overview of CRISPR-Cas9 delivery strategies and their trade-offs"
tags: [crispr, methods, gene-editing]
---

# Introduction

CRISPR-Cas9 has revolutionized genome editing, but getting the molecular machinery into cells remains a significant challenge. Different delivery methods come with distinct trade-offs in efficiency, toxicity, and off-target effects.

# Delivery Strategies

## Plasmid DNA Transfection

The traditional approach uses plasmid DNA encoding Cas9 and guide RNA. While straightforward, this method results in prolonged Cas9 expression, which can increase off-target editing.

## Ribonucleoprotein (RNP) Delivery

A more refined approach delivers pre-assembled Cas9 protein complexed with guide RNA directly into cells (1). This method offers several advantages:

- Rapid editing with transient Cas9 expression
- Reduced off-target effects
- No risk of plasmid integration
- Works well in hard-to-transfect cells

Recent work has also shown that Cas9 can process non-canonical crRNAs derived from host transcripts (2), opening new possibilities for RNA detection.

## mRNA Delivery

Delivering Cas9 as mRNA provides a middle ground—faster clearance than plasmid, but simpler preparation than RNP complexes.

# Conclusion

The choice of delivery method depends on your specific application. For most cell engineering applications, RNP delivery offers the best balance of efficiency and specificity.

# References

<div id="refs" class="references csl-bib-body">

<div id="ref-liang_rapid_2015" class="csl-entry">

<span class="csl-left-margin">1. </span><span class="csl-right-inline">Liang X, Potter J, Kumar S, Zou Y, Quintanilla R, Sridharan M, et al. Rapid and highly efficient mammalian cell engineering via Cas9 protein transfection. J Biotechnol \[Internet\]. 2015 Aug 20;208:44–53. Available from: <https://www.ncbi.nlm.nih.gov/pubmed/26003884></span>

</div>

<div id="ref-jiao_noncanonical_2021" class="csl-entry">

<span class="csl-left-margin">2. </span><span class="csl-right-inline">Jiao C, Sharma S, Dugar G, Peeck NL, Bischler T, Wimmer F, et al. Noncanonical <span class="nocase">crRNAs</span> derived from host transcripts enable multiplexable RNA detection by Cas9. Science \[Internet\]. 2021 Apr 27 \[cited 2021 May 24\]; Available from: <https://science.sciencemag.org/content/early/2021/04/26/science.abe7106></span>

</div>

</div>
