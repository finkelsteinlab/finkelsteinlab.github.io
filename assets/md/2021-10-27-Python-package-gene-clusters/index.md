---
layout: paper-md
title: "Opfi: A Python package for identifying gene clusters in large genomics and metagenomics data sets"
paper_slug: 2021-10-27-Python-package-gene-clusters
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/
pmcid: PMC9017871
---

# Opfi: A Python package for identifying gene clusters in large genomics and metagenomics data sets

**Alexis M. Hill\*, James R. Rybarski\*, Kuang Hu, Ilya J. Finkelstein, and Claus O. Wilke** (\* co-first authors)

*Journal of Open Source Software*, Volume 6, Issue 66, 3678 (2021)

**DOI:** [10.21105/joss.03678](https://doi.org/10.21105/joss.03678)

---

## Table of Contents

- [Summary](#summary)
- [Statement of Need](#statement-of-need)
- [Implementation](#implementation)
- [Acknowledgements](#acknowledgements)

---
##  Summary
Gene clusters are sets of co-localized, often contiguous genes that together perform specific functions, many of which are relevant to biotechnology. There is a need for software tools that can extract candidate gene clusters from vast amounts of available genomic data. Therefore, we developed Opfi: a modular pipeline for identification of arbitrary gene clusters in assembled genomic or metagenomic sequences. Opfi contains functions for annotation, de-deduplication, and visualization of putative gene clusters. It utilizes a customizable rule-based filtering approach for selection of candidate systems that adhere to user-defined criteria. Opfi is implemented in Python, and is available on the Python Package Index and on Bioconda ([Grüning et al., 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R6)).
---
##  Statement of need
Gene clusters have been successfully repurposed for a number of biotechnical applications, including biofuel production, organic compound synthesis, and gene editing ([Fischbach & Voigt, 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R5)). Despite the broad utility of known gene clusters, identification of novel gene clusters remains a challenging task. While there are many tools available for annotation of singular genes (or protein domains) in biological sequence data ([Buchfink et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R2); [Camacho et al., 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R3); [Steinegger & Söding, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R10)), these programs do not identify whole gene clusters out of the box. In many cases, researchers must combine bioinformatics tools ad hoc, resulting in one-off pipelines that can be difficult to reproduce. Several software packages have been developed for the discovery of specific types of gene clusters ([Blin et al., 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R1); [Santos-Aberturas et al., 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R8); [van Heel et al., 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R11)), but these tools may not be sufficiently flexible to identify clusters of an arbitrary genomic composition. To address these gaps, we developed a modular pipeline that integrates multiple bioinformatics tools, providing a flexible, uniform computational framework for identification of arbitrary gene clusters. In a recent study, we used Opfi to uncover novel CRISPR-associated transposons (CASTs) in a large metagenomics dataset ([Rybarski et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R7)).
---
##  Implementation
Opfi is implemented in Python, and uses several bioinformatics tools for feature annotation ([Buchfink et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R2); [Camacho et al., 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R3); [Edgar, 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R4); [Shi & Liang, 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R9); [Steinegger & Söding, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R10)). Users can install Opfi and all of its dependencies through Bioconda ([Grüning et al., 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R6)). Opfi consists of two major components: Gene Finder, for discovery of gene clusters, and Operon Analyzer, for rule-based filtering, deduplication, and visualization of gene clusters identified by Gene Finder. All modules generate output in a comma-separated (CSV) format that is common to the entire package.
### Example Gene Finder usage
The following example script searches for putative CRISPR-Cas loci in the genome of _Rippkaea orientalis PCC 8802_. Information about the biological significance of this example, as well as data inputs and descriptions, can be found in the tutorials directory in the project GitHub repository. The example illustrates the use of the Pipeline class for setting up a gene cluster search. First, add_seed_step specifies a step to annotate _cas1_ genes, using protein BLAST (BLASTP) ([Camacho et al., 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R3)) and a database of representative Cas1 protein sequences. 10,000 bp regions directly up- and downstream of each putative _cas1_ gene are selected for further analysis, and all other regions are discarded. Next, add_filter_step adds a step to annotate candidate regions for additonal _cas_ genes. Candidates that do not have at least one additional _cas_ gene are discarded from the master list of putative systems. Finally, add_crispr_step adds a step to search remaining candidates for CRISPR arrays, i.e. regions of alternating ~30 bp direct repeat and variable sequences, using the PILER-CR repeat finding software ([Edgar, 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R4)).
![graphic file with name nihms-1796212-f0002.jpg](nihms-1796212-f0002.jpg)
Running this code creates the CSV file r_orientalis_results.csv, which contains information about each system identified; in this example, that is two canonical CRISPR-Cas systems, and one locus with weak homology to _cas_ genes. Each line in the file represents a single putative feature in a candidate locus. Features from the same candidate are grouped together in the CSV. Detailed information about the output format can be found in the Opfi documentation.
### Example Operon Analyzer usage
In the previous example, passing systems must meet the relatively permissive criterion of having at least one _cas1_ gene co-localized with one additional _cas_ gene. This is sufficient to identify CRISPR-Cas loci, but may also capture regions that do not contain functional CRISPR-Cas systems, but rather consist of open reading frames (ORFs) with weak homology to _cas_ genes.
These improbable systems could be eliminated during the homology search by making the match acceptance threshold more restrictive (i.e., by decreasing the e-value), however, this could result in the loss of interesting, highly diverged systems. Therefore, we implemented a module that enables post-homology search filtering of candidate systems, using flexible rules that can be combined to create sophisticated elimination functions. This allows the user to first perform a broad homology search with permissive parameters, and then apply rules to cull unlikely candidates without losing interesting and/or novel systems. Additionally, rules may be useful for selecting candidates with a specific genomic composition for downstream analysis. It should be noted that the use of the term “operon” throughout this library is an artifact from early development of Opfi. At this time, Opfi does not predict whether a candidate system represents a true operon, that is, a set of genes under the control of a single promoter. Although a candidate gene cluster may certainly qualify as an operon, it is currently up to the user to make that distinction.
Rule-based filtering is illustrated with the following example. The sample script takes the output generated by the previous example and reconstructs each system as an Operon object. Next, the RuleSet class is used to assess each candidate; here, passing systems must contain two cascade genes (_cas5_ and _cas7_) no more than 1000 bp apart, and at least one _cas3_ (effector) gene. For a complete list of rules, see the Opfi [documentation](https://opfi.readthedocs.io/).
![graphic file with name nihms-1796212-f0003.jpg](nihms-1796212-f0003.jpg)
After running this code, the file filtered_output.csv contains only high-confidence type-I CRISPR-Cas systems (re-serialized to CSV format) that passed all rules in the rule set.
### Candidate visualization
Opfi integrates the DNAFeaturesViewer package ([Zulkower & Rosser, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#R12)) to create gene diagrams of candidate systems. Each input system is visualized as a single PNG image. The sample script below reads in output from the previous example, and generates two gene diagram images, one for each CRISPR-Cas system present in _Rippkaea orientalis_. One image is provided for reference in [Figure 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/#F1).
#### Figure 1: {#fig1}
![Figure 1](nihms-1796212-f0001.jpg)
One of two type-I CRISPR-Cas systems present in the genome of _Rippkaea orientalis PCC 8802_. Note that the ORF beginning at position ~2500 has homology with both _cas1_ and _cas4_. These alignments have identical bitscores (i.e., the goodness of alignments is quivalent, using this metric), so both annotations appear in the diagram, even though pick_overlapping_features_by_bit_score was applied.
![graphic file with name nihms-1796212-f0004.jpg](nihms-1796212-f0004.jpg)
![graphic file with name nihms-1796212-f0005.jpg](nihms-1796212-f0005.jpg)
The FilterSet class is used to resolve features with sequences that overlap by more than 90%. Specifically, only the overlapping feature with the highest bitscore value (a quantity that describes the overall quality of an alignment) is rendered when pick_overlapping_fea tures_by_bit_score is applied. Note that is not a requirement for candidate visualization, but can improve gene diagram clarity.
---
##  Acknowledgements
The authors would like to thank the staff of the Texas Advanced Computing Center for providing computational resources, and members of the Finkelstein and Wilke labs for helpful discussions. This work was supported by an NIGMS grant R01GM124141 (to I.J.F.), the Welch Foundation grant F-1808 (to I.J.F.), NIGMS grant R01 GM088344 (to C.O.W.), and the College of Natural Sciences Catalyst Award for seed funding.

---

## References

1. Blin K, Shaw S, Steinke K, Villebro R, Ziemert N, Lee SY, Medema MH, & Weber T (2019). "antiSMASH 5.0: updates to the secondary metabolite genome mining pipeline." Nucleic Acids Research, 47(W1), W81–W87. doi: 10.1093/nar/gkz310
2. Buchfink B, Reuter K, & Drost H-G (2021). "Sensitive protein alignments at tree-of-life scale using DIAMOND." Nature Methods, 18(4), 366–368. doi: 10.1038/s41592-021-01101-x
3. Camacho C, Coulouris G, Avagyan V, Ma N, Papadopoulos J, Bealer K, & Madden TL (2009). "BLAST+: Architecture and applications." BMC Bioinformatics, 10(1), 421. doi: 10.1186/1471-2105-10-421
4. Edgar RC (2007). "PILER-CR: Fast and accurate identification of CRISPR repeats." BMC Bioinformatics, 8(1), 18. doi: 10.1186/1471-2105-8-18
5. Fischbach M, & Voigt CA (2010). "Prokaryotic gene clusters: A rich toolbox for synthetic biology." Biotechnology Journal, 5(12), 1277–1296. doi: 10.1002/biot.201000181
6. Grüning B, Dale R, Sjödin A, Chapman B, Rowe J, Tomkins-Tinch CH, Valieris R, Köster J, & The Bioconda Team (2018). "Bioconda: sustainable and comprehensive software distribution for the life sciences." Nature Methods, 15(7), 475–476. doi: 10.1038/s41592-018-0046-7
7. Rybarski JR, Hu K, Hill AM, Wilke CO, & Finkelstein IJ (2021). "Metagenomic discovery of CRISPR-associated transposons." bioRxiv. doi: 10.1101/2021.08.16.456562
8. Santos-Aberturas J, Chandra G, Frattaruolo L, Lacret R, Pham TH, Vior NM, Eyles TH, & Truman AW (2019). "Uncovering the unexplored diversity of thioamidated ribosomal peptides in Actinobacteria using the RiPPER genome mining tool." Nucleic Acids Research, 47(9), 4624–4637. doi: 10.1093/nar/gkz192
9. Shi J, & Liang C (2019). "Generic Repeat Finder: A High-Sensitivity Tool for Genome-Wide De Novo Repeat Detection." Plant Physiology, 180(4), 1803–1815. doi: 10.1104/pp.19.00386
10. Steinegger M, & Söding J (2017). "MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets." Nature Biotechnology, 35(11), 1026–1028. doi: 10.1038/nbt.3988
11. van Heel AJ, de Jong A, Song C, Viel JH, Kok J, & Kuipers OP (2018). "BAGEL4: a user-friendly web server to thoroughly mine RiPPs and bacteriocins." Nucleic Acids Research, 46(W1), W278–W281. doi: 10.1093/nar/gky383
12. Zulkower V, & Rosser S (2020). "DNA Features Viewer: a sequence annotation formatting and plotting library for Python." Bioinformatics, 36(15), 4350–4352. doi: 10.1093/bioinformatics/btaa213

---

*Archived from [PubMed Central (PMC9017871)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9017871/) on 2025-07-19.*
