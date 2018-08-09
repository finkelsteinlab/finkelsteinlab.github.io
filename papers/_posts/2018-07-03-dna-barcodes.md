---
layout: paper
title: "Indel-correcting DNA barcodes for high-throughput sequencing."
volume: 115
issue: 27
pages: E6217-26
year: "2018"
shortref: "Hawkins _et al._ PNAS (2018)"
nickname: "dna-barcodes"
journal: "Proc Natl Acad Sci USA"
authors: "John A. Hawkins, Stephen K. Jones Jr., Ilya J. Finkelstein&dagger;, and William H. Press&dagger; (&dagger; co-corresponding)"
pdf: 0042-2018-PNAS-Hawkins et al.pdf
supplement: 0042-2018-PNAS-Hawkins et al-supplement.pdf
doi: 10.1073/pnas.1802640115
pmcid:
pmid: 29925596
extra_text: '
**Press:**

  * [DNA Barcodes That Work (CNS)](https://cns.utexas.edu/news/dna-barcodes-that-reliably-work-a-game-changer-for-biomedical-research)  

  * [Method makes DNA barcodes way more reliable (Futurity)](https://www.futurity.org/dna-barcode-1799862/)  

  * [Reliable DNA barcodes (Phys.org)](https://phys.org/news/2018-06-dna-barcodes-reliably-game-changer-biomedical.html)  

  * [Eureka Alert](https://www.eurekalert.org/pub_releases/2018-06/uota-dbt062018.php)  



'
category: paper
tags: [DNA barcodes, Error-correcting codes, Information storage, Massively parallel synthesis]
---
{% include JB/setup %}

# Abstract

Many large-scale, high-throughput experiments use DNA barcodes, short DNA sequences prepended to DNA libraries, for identification of individuals in pooled biomolecule populations. However, DNA synthesis and sequencing errors confound the correct interpretation of observed barcodes and can lead to significant data loss or spurious results. Widely used error-correcting codes borrowed from computer science (e.g., Hamming, Levenshtein codes) do not properly account for insertions and deletions (indels) in DNA barcodes, even though deletions are the most common type of synthesis error. Here, we present and experimentally validate filled/truncated right end edit (FREE) barcodes, which correct substitution, insertion, and deletion errors, even when these errors alter the barcode length. FREE barcodes are designed with experimental considerations in mind, including balanced guanine-cytosine (GC) content, minimal homopolymer runs, and reduced internal hairpin propensity. We generate and include lists of barcodes with different lengths and error correction levels that may be useful in diverse high-throughput applications, including >106 single-error-correcting 16-mers that strike a balance between decoding accuracy, barcode length, and library size. Moreover, concatenating two or more FREE codes into a single barcode increases the available barcode space combinatorially, generating lists with >1015 error-correcting barcodes. The included software for creating barcode libraries and decoding sequenced barcodes is efficient and designed to be user-friendly for the general biology community.
