---
layout: paper-md
title: "High-Throughput Universal DNA Curtain Arrays for Single-Molecule Fluorescence Imaging."
paper_slug: 2015-09-22-dna-curtain-arrays
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4624423/
pmcid: PMC4624423
---

# High-Throughput Universal DNA Curtain Arrays for Single-Molecule Fluorescence Imaging

**Ignacio F. Gallardo, Praveenkumar Pasupathy, Maxwell Brown, Carol M. Manhart, Dean P. Neikirk, Eric Alani, and Ilya J. Finkelstein**

*Langmuir*, Volume 31, Issue 37, Pages 10310–7 (2015)

**DOI:** [10.1021/acs.langmuir.5b02416](https://doi.org/10.1021/acs.langmuir.5b02416)

---

## Table of Contents

- [Abstract](#abstract)
- [Introduction](#introduction)
- [Experimental Section](#experimental-section)
- [Results and Discussion](#results-and-discussion)
- [Conclusions](#conclusions)
- [Acknowledgments](#acknowledgments)

---

## Abstract
Single-molecule studies of protein–DNA interactions have shed critical insights into the molecular mechanisms of nearly every aspect of DNA metabolism. The development of DNA curtains—a method for organizing arrays of DNA molecules on a fluid lipid bilayer—has greatly facilitated these studies by increasing the number of reactions that can be observed in a single experiment. However, the utility of DNA curtains is limited by the challenges associated with depositing nanometer-scale lipid diffusion barriers onto quartz microscope slides. Here, we describe a UV lithography-based method for large-scale fabrication of chromium (Cr) features and organization of DNA molecules at these features for high-throughput single-molecule studies. We demonstrate this approach by assembling 792 independent DNA arrays (containing >900 000 DNA molecules) within a single microfluidic flowcell. As a first proof of principle, we track the diffusion of Mlh1-Mlh3—a heterodimeric complex that participates in DNA mismatch repair and meiotic recombination. To further highlight the utility of this approach, we demonstrate a two-lane flowcell that facilitates concurrent experiments on different DNA substrates. Our technique greatly reduces the challenges associated with assembling DNA curtains and paves the way for the rapid acquisition of large statistical data sets from individual single-molecule experiments.
![Graphical Abstract](nihms731807f6.jpg)

---
## INTRODUCTION
Single-molecule fluorescence imaging approaches have shed critical insights into numerous biological processes and have proven especially useful for understanding DNA transcription, replication, and repair.[[1–6](#ref1)] However, acquiring statistically relevant data sets remains a challenge for experiments that are performed on one molecule at a time. The recently developed “DNA curtains” platform overcomes this limitation by permitting the observation of hundreds of biochemical reactions in real time.[[7](#ref7)],[[8](#ref8)] In this approach, individual DNA molecules are anchored to a supported lipid bilayer (SLB) via a biotin–streptavidin interaction and aligned along barriers to lipid diffusion by the application of hydrodynamic force (see [Figure 1](#fig1) for schematic).[[7](#ref7)] The immobilized DNA and proteins are imaged via total internal reflection fluorescence (TIRF) microscopy ([Figure 1A](#fig1)). This experimental platform has recently been applied to a number of biochemical problems related to protein–DNA interactions.[[9–11](#ref9)]

<figure class="paper-figure" id="fig1">
<img src="nihms731807f1.jpg" alt="Figure 1">
<figcaption><strong>Figure 1. An illustration of the DNA curtains platform.</strong> (A) DNA molecules are immobilized on the passivated surface of a microfluidic flowcell. The DNA is illuminated via a laser beam (488 nm) that impinges on a prism in total internal reflection fluorescence (TIRF) mode, thereby generating an evanescent excitation wave at the interface between the lithographic patterned surface and the imaging buffer. The evanescent wave penetrates ~200 nm away from the micropatterned flowcell surface to selectively illuminate surface-bound DNA and protein molecules. The resulting fluorescent signals propagate through a coverslip and are collected via a high numerical aperture objective, passed through two excitation clean-up filters (490 and 500 long pass; Chroma), and dispersed through a dichromic mirror onto two different charge coupled device (CCD; ANDOR) cameras. (B) Side view of a DNA molecule (green) that is affixed to a lipid bilayer (circles) via a biotin–streptavidin (magenta) linkage. In the presence of buffer flow, the DNA molecule moves within the fluid lipid bilayer and is captured at a Cr diffusion barrier (gray).</figcaption>
</figure>
Supported lipid bilayers have emerged as versatile surfaces for assembling DNA curtains and offer multiple advantages for single-molecule studies of protein–DNA interactions.[[12](#ref12)] First, the SLB charge is readily tunable by changing the lipid composition and zwitterionionic head groups.[[13](#ref13)] Second, the bilayers can be doped with biotin, poly(ethylene glycol)s, and other exogenous chemicals.[[14](#ref14)],[[15](#ref15)] The biomimetic lipid bilayer also provides excellent surface passivation, thereby preventing nonspecific adsorption of nucleic acids, and proteins to the flowcell surfaces.[[12](#ref12)],[[16](#ref16)],[[17](#ref17)] Finally, lipid bilayers are readily manipulated via external shear or electrophoretic forces, and the bilayers can be corralled at mechanical barriers to lipid diffusion.[[18–25](#ref18)]
The ability to manipulate and organize SLBs at mechanical barriers is at the core of the DNA curtains single-molecule platform. However, widespread adoption of DNA curtains has been hampered by the difficulty of fabricating custom microscope slides that are required for organizing arrays of DNA molecules. Early approaches used a glass scribe to mechanically etch such barriers,[[18](#ref18)],[[26](#ref26)] but in practice hand-etching does not produce controllable lipid diffusion barriers. Microcontact printing of protein barriers has also been used to rapidly fabricate lipid diffusion barriers, but these surface features are either too large (>10 µm) or are readily removed during stringent wash cycles.[[27–31](#ref27)] To overcome these limitations, an electron beam lithography (EBL)-based fabrication strategy has been used to deposit chromium (Cr) patterns on glass slides.[[32](#ref32)],[[33](#ref33)] EBL is a high-resolution but low-throughput fabrication method because it requires raster scanning of an electron beam along each segment of the nanobarrier,[[34](#ref34)],[[35](#ref35)] thereby limiting the number of barriers that are deposited onto each quartz slide. The low-throughput nature of EBL, coupled with the high cost and limited availability of this specialized instrument, prompted us to develop a new approach for depositing Cr patterns on quartz microscope slides for DNA curtain imaging.
Here, we describe a UV lithography-based process for large-scale fabrication of Cr features for assembling DNA curtains.[[36](#ref36)],[[37](#ref37)] Using this fabrication method, we organize hundreds of thousands of DNA molecules within a single flowcell for high-throughput single-molecule imaging. The UV-patterned flowcells are capable of organizing aligned arrays of both single- and double-stranded DNA molecules. By patterning a large flowcell area, we also demonstrate multichannel microfluidic flowcells with two different DNA substrates. As our approach is both rapid and does not require advanced EBL or nanoimprint lithography apparatus, it will facilitate the adoption of high-throughput DNA curtains by the broader biophysical and analytical biosensor communities.

---

## EXPERIMENTAL SECTION
### Quartz Wafer Fabrication
Chrome diffusion barriers were made on 1.58 mm thick, 101.6 mm diameter ground and polished GE124 quartz disks (Technical Glass Products). A flat was made by grinding 2 mm into the glass. Glass wafers were sequentially rinsed with acetone, isopropanol, and water and dried with a stream of N₂ gas. The wafers were spin-coated in a Lauell Technologies Spinner, (4000 rpm for 45 s) with a layer of photoresist (Clariant, AZ5209E). The coated wafer was heated to 95 °C on a hot plate for 2 min. UV lithography was performed using a SUSS Microtec -MA6/BA6 mask aligner (MA6, hard contact mode, 6.5 s at 6.5 mW cm⁻²) using a chrome-coated quartz mask (Photo Sciences). AutoCAD files of the quartz masks are available upon request. The photoresist layer was developed by rinsing the wafer in developer (Megaposit MF-26A; 2–2.5% tetramethylammonium hydroxide (TMAH), DOW Chemical Company) for 35–40 s. The wafer was rinsed in deionized water and dried in N₂ flow. After development, the wafers were etched with oxygen plasma for 120 s at 100 W (March CS-1701 etcher) to remove all the residual photoresist from the developed surface. A 20 nm layer of chromium (99.998% Kurt J. Lesker) was then sputtered onto the wafer (Cooke E-beam/ sputter deposition system at 8 kV). To lift off the photoresist and chromium, the wafer was sonicated in acetone for 1 min, rinsed in ethanol, and dried in N₂ flow. The wafers were covered with a clean-room-rated silicon wafer tape (ICROS) and diced into six flowcell sized (50 mm × 22 mm) substrates (Disco 321 dicing saw).
### Proteins and DNA
Plasmids overexpressing human RPA-GFP were generously provided by Dr. Mauro Modesti and purified essentially as described previously.[[38](#ref38)] Phi29 DNA polymerase and FLAG-epitope labeled _S. cerevisiae_ Mlh1-Mlh3 were purified as described previously.[[39](#ref39)],[[40](#ref40)] Histones H2A, H2B, H3, and H4 were purified as described.[[41](#ref41)],[[42](#ref42)] For fluorescent labeling, H2A encodes an Nterminal 3xFLAG epitope tag. Detailed protocols for preparing DNA substrates for single-molecule imaging are described in the Supporting Information.
### Nucleosome Reconstitution
#### Histone Octamer Assembly
Each of the four histones was dissolved in unfolding buffer (20 mM Tris-HCl pH 7.5, 7 M guanidinium-HCl, and 10 mM DTT) and gently agitated for 1 h at RT. The histones were mixed in equimolar ratios of H3/H4 and a 10% higher molar ratio of H2A/H2B relative to H3/ H4). The mixture was adjusted to a final concentration of 1 mg/mL and dialyzed against refolding buffer (10 mM Tris-HCl pH 8.0, 1 mM EDTA, 5 mM β-mercaptoethanol, 2 M NaCl) using 3500 MWCO dialysis tubing with several buffer exchanges over 48 h. The dialyzed mixture was centrifuged to remove aggregates and concentrated using spin concentrators (Amicon Ultra-15; Millipore) to a final volume of about 1 mL. Gel filtration over a Superdex-200 (GE Healthcare) using SAU-200 was performed to resolve histone octamers from dimers and tetramers in the refolding buffer. The octamer peak fractions were combined, concentrated using a 10 000 MWCO spin concentrator (Amicon Ultra-4, Millipore), and flash frozen using liquid N₂. The resulting histone octamers were stored in −80 °C until use.
#### Nucleosome Reconstitution
Human nucleosomes were reconstituted on the λ-phage DNA via stepwise salt dialysis.[[42](#ref42)],[[43](#ref43)] First, λ-phage DNA was ligated to biotinylated and DIG-terminated oligonucleotides (IF7 and IF9, respectively) and gel-filtered through an S-1000 column (GE). The DNA was concentrated using isopropanol precipitation and dissolved to a final concentration of 70 ng µL⁻¹ in TE with high salt (10 mM Tris-HCl pH 8.0, 1 mM EDTA, 2 M NaCl). For reconstitution, 30 µL of the DNA (final concentration of ~20 ng µL⁻¹) was used in total volume of 100 µL. The octamer was diluted 10-fold in dilution buffer (10 mM Tris-HCl pH 7.6, 1 mM EDTA, 2 M NaCl) right before use. The 100 µL mixture was dialyzed using a mini dialysis button (10K MWCO, BioRad) against 400 mL of storage buffer (10 mM Tris-HCl pH 7.6, 1 mM EDTA, 1 mM DTT) that contained gradually decreasing concentrations of NaCl. Dialysis was performed in a cold room at 4 °C for at least 90 min at each step: 1.5, 1, 0.8, 0.6, and 0.4 M NaCl. As a final step, the reaction was dialyzed into 0.2 M NaCl overnight. At a nominal input ratio of 1:75 (DNA:octamer), we counted about 1–5 nucleosomes per DNA molecules. The large nominal DNA:octamer ratio probably stems from octamer loss due to aggregation onto the dialysis membrane and polypropylene tubing during the extended dialysis procedure.[[43](#ref43)] The nucleosome-coated DNA was stored at 4 °C for up to 2 weeks.
#### Single Molecule Microscopy
Flowcells and DNA curtains were assembled accordingly to previously published protocols, with some modifications (see Supporting Information).[[7](#ref7)] Images were collected with a Nikon Ti-E microscope in a prism-TIRF configuration. The inverted microscope setup allowed for the sample to be illuminated by a 488 nm laser light (Coherent) through a quartz prism. To minimize spatial drift, the experiment was conducted on a floating TMC optical table. A 60× water immersion objective lens (1.2 NA, Nikon), two EMCCD cameras (Andor iXon DU897, cooled to −80 °C), and Nis Elements software (Nikon) were used to collect the data with a 200 ms frame rate. Frames were saved as TIFF files without compression, and further image analysis was done in ImageJ (NIH).
### Observing Fluorescent Mlh1-Mlh3 on DNA Curtains
To fluorescently label Mlh1-Mlh3, 60 nM of the protein complex was mixed with 120 nM anti-FLAG QDs (QD705, Life Technologies) and incubated in 10 µL of imaging buffer for 15 min on ice. The Mlh1-Mlh3-QD mixture was diluted 6-fold in imaging buffer and injected into the flowcells via a 50 µL injection loop (at a flow rate of 50 µL min⁻¹) and the flowcell flushed thoroughly at a flow rate of 300 µL min⁻¹ to remove all Mlh1-Mlh3 molecules that did not associate with the DNA curtains. Then buffer flow was stopped, and a movie was collected at a 200 ms frame rate. We did not fluorescently label the DNA during the diffusion experiments. To ensure that the fluorescent Mlh1-Mlh3 trajectories corresponded to DNA-bound proteins, the DNA molecules were stained with YOYO-1 after the completion of each diffusion experiment. Only DNA-bound QDs were analyzed. Fluorescent Mlh1-Mlh3 was tracked in ImageJ (NIH) with a custom-written particle tracking script. For each frame the fluorescent particle was fit to a two-dimensional Gaussian function to obtain trajectories with subpixel resolution. The resulting trajectories were analyzed in Matlab (Mathworks). The mean-squared displacement and diffusion coefficients were calculated as described previously.[[44](#ref44)]
### Dual-Channel Flowcells
To assemble the dual-channel flowcells, microfabricated quartz slides were drilled with two inlet ports and a single outlet port. Y-shaped double-sided sticky tape (700 µm nominal thickness, type 666 from 3M) was cut using an Exacto and sandwiched between the quartz slide and a microscope coverslip. After baking the flowcell at 140 °C for 60 min, each ~9 mm lane was separated by a 2 mm barrier. The lipid bilayers were deposited through the inlet ports of lanes 1 and 2 (Figure S4A) keeping the single outlet port of the flowcell closed. To inject different DNA substrates into each of the lanes, the outlet port was opened, and 1 mL of an ~1 pM concentration of each DNA substrate was injected through the inlet ports (Figure S4A). Both DNA solutions were injected in parallel to prevent backflow between the two inlet channels (and cross-mixing between different types of DNA). Fluorescent labeling of the 3xFlag-tagged histone H2A was conducted as described for Mlh1-Mlh3 (see above). At the microscope, the antibody-QD solution was injected at 200 µL min⁻¹ with a 700 µL loop (using a Rheodyne MXP7900 valve) between the syringe and the lane containing nucleosomes (Figure S4B). The imaging buffer had 0.2 nM of YOYO-1 and was injected at 400 µL min⁻¹ into each flowcell (Figure S4B). Images were taken after the free antibody had been washed out the flowcells. Frames were taken every 200 ms when the buffer flow was 400 µL min⁻¹. Two additional valves (shut-off valve; IDEX Health Science) were added right before the input of each lane to independently stop each flow. A computer-controlled microscope stage (Prior ProScan II) was used to sequentially image the two lanes with a 1 s frame rate.

---

## RESULTS AND DISCUSSION
We developed a UV lithography-based process for large-scale fabrication of quartz substrates for DNA curtain imaging ([Figure 2A](#fig2)). In this approach, quartz wafers are coated with a UV-sensitive photoresist, exposed through a high-resolution photomask, and then developed (see Experimental Section). Next, an ~20 nm layer of Cr is deposited onto the wafer, and a lift-off procedure is used to remove all Cr that is not affixed to the quartz surface. Finally, the wafers are diced into 50 mm × 22 mm quartz slides, and each slide is drilled to produce individual microfluidic flowcells. As this process can pattern the surface of an entire wafer with a single UV exposure, we increased both the quantity and the types of diffusion barriers per microscope slide. [Figure 2B](#fig2) shows an optical image of a subset (72 in the figure), of the 792 total barrier sets that were deposited within each of the microfluidic flowcells. Individual barrier sets were highly uniform over the whole flowcell area ([Figure 2C,D](#fig2)). Atomic force microscopy ([Figure 2E](#fig2)) and scanning electron microscopy (Supporting Information Figure S1) confirmed that the UV-lithography barriers retained excellent uniformity and that the quartz slides were largely free of Cr and other fabrication defects. Although our UV lithography process is currently limited to ~1 µm wide surface features, this does not significantly impact the assembly or imaging of the 16 µm long DNA substrates (see below). With further optimization, conventional contact-mode UV lithography can be used to produce ~200 nm wide features.[[45](#ref45)],[[46](#ref46)] Importantly, this process is substantially more rapid, cost-effective, and easier to implement than EBL. The layout of the Cr features can be readily changed by ordering the appropriate UV photomask, and each 106 mm wafer is diced to produce six microfluidic flowcells. We conclude that UV photolithography can be used to rapidly fabricate Cr diffusion barriers for singlemolecule DNA curtains.

<figure class="paper-figure" id="fig2">
<img src="nihms731807f2.jpg" alt="Figure 2">
<figcaption><strong>Figure 2. Chromium barriers are deposited via UV lithography.</strong> (A) First, a quartz wafer is coated with photoresist and exposed to UV light through a high-resolution (chrome-on-quartz) UV photomask in contact mode geometry. The UV resist is developed, and 20 nm of Cr is deposited onto the wafer. Excess Cr is lifted off by gently dissolving the residual developer in acetone, leaving behind only the Cr that had bonded directly to the quartz surface. Finally, the wafer is diced to generate six (~22 mm × ~50 mm) quartz slides. Each slide is drilled using a diamond-coated drill bit to allow fluidic access to the flowcells. (B) An optical image of 72 barrier sets (from a total of 792 barrier sets) that are deposited onto each flowcell. Scale bar: 1 mm. A close-up view of a set of barriers used for single-tethering (C) and double-tethering DNA (D). The barriers sets are nearly free of residual Cr and other fabrication defects. Scale bars in (C) and (D) are 50 µm. (E) An AFM scan of the rectangular region in (D) shows that the Cr barriers have an average height of 20 nm.</figcaption>
</figure>
Assembling DNA curtains requires a fluid SLB, which is critically dependent on the surface chemistry of the quartz substrate.[[18](#ref18)],[[47](#ref47)],[[48](#ref48)] We therefore tested whether the microfabrication process adversely affects DNA curtain assembly on UV-patterned slides ([Figure 3](#fig3)). First, lipid vesicles were incubated in the flowcell. Vesicles rupture and fusion facilitates the formation of continuous sheets of fluid SLBs.[[49](#ref49)] One end of each DNA molecule was affixed to the SLB via a biotin– streptavidin linkage, and buffer flow was used to organize and extend individual DNA molecules at the Cr barriers ([Figure 3B](#fig3)). When buffer flow was turned off, all DNA molecules collapsed to the tether point at the Cr diffusion barrier ([Figure 3C](#fig3)). We further confirmed that these flowcells are also compatible with ssDNA curtains (Figure S2).[[39](#ref39)],[[50](#ref50)] To generate ssDNA curtains, we prepared a plasmid where one strand contained a biotinylated 5′-ssDNA flap (Figure S2A; see Supporting Information). This biotinylated DNA substrate was used as a template for rolling circle replication (RCR) with phi29 DNA polymerase.[[39](#ref39)] The resulting ssDNA molecules were readily assembled at the microfabricated diffusion barriers and were visualized with GFP-labeled replication protein A (RPA), a heterotrimeric protein complex that binds ssDNA (Figure S2B).[[39](#ref39)],[[50](#ref50)] Together, these results demonstrate that lipid bilayers maintain their fluidity on UV-fabricated quartz slides and that these slides can be used for large-scale organization of both dsDNA and ssDNA molecules.

<figure class="paper-figure" id="fig3">
<img src="nihms731807f3.jpg" alt="Figure 3">
<figcaption><strong>Figure 3. UV-fabricated Cr barriers support the assembly of DNA curtains.</strong> (A) An illustration of single-tethered DNA curtains. A fluid lipid bilayer (yellow) is deposited onto the micropatterned quartz surface (blue). DNA (green) is anchored to the lipid bilayer at one end, and buffer flow is used to organize the DNA molecules at the Cr diffusion barriers (gray). (B) A 170 × 103 µm field of view with individual DNA molecules (derived from λ-phage, ~48 500 bp long) assembled at five Cr barriers (red triangles). The DNA molecules are stained with the fluorescent intercalating dye YOYO-1 (Life Tech.), and there are >1200 DNA molecules within this field of view. (C) In the absence of buffer flow, the extended DNA molecules retract to the barriers. Scale bar: 20 µm.</figcaption>
</figure>
To maximize the types of experiments that can be conducted within a single microfabricated flowcell, we also deposited a subset of barriers with additional pedestals that facilitate tethering of the DNA molecules by both ends. These double-tethered DNA molecules remain extended without any buffer flow, permitting the observation of protein–DNA interactions without continuous application of a hydrodynamic force ([Figure 4A](#fig4)).[[32](#ref32)] For double tethering, one end of the DNA was labeled with a biotin and the second end was labeled with a digoxigenin (DIG).[[7](#ref7)] We patterned the quartz slides with pedestals that were deposited 13 µm away from the diffusion barriers. These pedestals were first decorated with a goat antirabbit antibody (Immunology Consultants Laboratory, Inc.), followed by a primary rabbit anti-DIG antibody (ABfinity, Life Tech.). The primary–secondary antibody pair serves as an attachment point for DNA molecules that present their DIG ends near these pedestals (see Supporting Information for detailed methods). [Figure 4B](#fig4) shows that individual DNA molecules were readily tethered between the barriers and pedestals. In the absence of buffer flow, the double-tethered DNA molecules remained fully extended for 29 ± 0.2 min (half-life ± standard error, _N_ = 163; Figure S3). Gradual loss of double-tethered DNA may be due to (i) photodamage-induced DNA breaks, (ii) removal of the biotinylated lipid from the SLB, (iii) disruption of antibody–antigen interactions (either DIG-antibody or primary/secondary interactions), and (iv) desorption of the secondary antibody from the Cr pedestals. We confirmed that the double-tethering lifetime was identical when the laser was shuttered at 1 or 5 min intervals (data not shown), indicating that laser-induced DNA damage is not the primary cause of the observed lifetime. Based on the force– extension curve of λ-phage DNA,[[51](#ref51)] individual molecules are under ~0.5–2 pN of tension when extended to a length of 12– 14 µm (corresponding to the minimum and maximum distance between the Cr barrier and pedestal). Lipid-rupture forces are in the ~20 pN range, suggesting that loss of the biotinylated lipid is also unlikely.[[52–55](#ref52)] We favor a model where the DNA is lost due to rupture of the antibody–antigen interactions, as the observed lifetime is consistent with the off rates (*k*<sub>off</sub>) reported for antibody–DIG interaction.[[56](#ref56)],[[57](#ref57)] We cannot rule out that double-tethered DNA molecule are also lost due to desorption of the secondary antibodies from Cr pedestals. Regardless, the observed lifetime is sufficient for many experiments involving protein–DNA interactions (see below). Incorporating handles with multiple DIG molecules to increase the total number of DNA–pedestal tethers may further increase the double-tethered DNA lifetime.[[58–60](#ref58)]

<figure class="paper-figure" id="fig4">
<img src="nihms731807f4.jpg" alt="Figure 4">
<figcaption><strong>Figure 4. Illustration of the scheme used for double-tethering DNA molecules on UV-fabricated Cr barriers.</strong> (A) The DNA is functionalized with biotin at one end and digoxigenin (DIG) at the other end. To extend and immobilize the DNA by both ends, oval-shaped Cr pedestals (1.3 × 1.5 µm; gray) are deposited 13 µm away from the linear barriers. Pedestals and barriers have the same Cr height. Secondary antirabbit antibodies (red) are adsorbed onto the pedestals. Primary rabbit anti-DIG antibodies (blue) are washed through the flowcell and captured by the secondary antibodies. Finally, the λ-DNA is tethered to the lipid bilayer surface via a biotin–streptavidin linkage, pushed to the barriers, and anchored on the pedestal via a DIG– antibody interaction. (B) Fluorescent DNA molecules (green) that remain fully extended between the barriers (red triangle) and oval pedestals (red circle) in the absence of buffer flow. Fluorescent Mlh1-Mlh3 (magenta; labeled with a QD) binds the DNA molecules. In the absence of buffer flow, Mlh1-Mlh3 diffuses freely on the extended DNA. Scale bar: 5 µm. (C) Kymograph of a representative Mlh1-Mlh3 (black) diffusing on DNA. Blinking of the fluorescence signal (blue arrows) indicates that Mlh1-Mlh3 is labeled with a single QD. To avoid photodamage, the DNA is not fluorescently labeled. (D) The mean-squared displacement (MSD) of five diffusing Mlh1-Mlh3 molecules. A linear fit to the MSD curves is used to calculate the diffusion coefficient of each molecule.</figcaption>
</figure>
To demonstrate that UV-fabricated slides can support single-molecule studies of protein–DNA interactions, we monitored the DNA binding properties of _S. cerevisiae_ Mlh1-Mlh3 on double-tethered DNA curtains. Mlh1-Mlh3 is a heterodimeric protein complex that participates in DNA mismatch repair and in resolution of meiotic recombination intermediates.[[40](#ref40)],[[61](#ref61)],[[62](#ref62)] To fluorescently label Mlh1-Mlh3, we exploited a single FLAG epitope tag that has been inserted after amino acid 448 in Mlh1. Previous studies have shown that Mlh1 maintains full biochemical activity with this FLAG epitope.[[40](#ref40)],[[63](#ref63)] The Mlh1 subunit was fluorescently labeled by conjugating the enzyme with an anti-FLAG antibody covalently linked to a quantum dot (QD; Life Tech.), as described previously.[[64](#ref64)] [Figure 4B](#fig4) shows that fluorescently labeled Mlh1-Mlh3 was able to bind to the double-tethered DNA molecules. Mlh1-Mlh3 readily diffused on the DNA ([Figure 4C,D](#fig4)), and the diffusion coefficient was 0.026 ± 0.03 µm² s⁻¹ (mean ± std dev; _N_ = 25). The Mlh1-Mlh3 diffusion coefficients are within the range reported for other mismatch repair complexes, including the Mlh1-Pms1 complex (0.020 ± 0.023 µm² s⁻¹ at 50 mM NaCl),[[65](#ref65)] suggesting that both complexes may share similar diffusive behaviors on dsDNA.[[64](#ref64)],[[65](#ref65)] Proteins scan DNA via several facilitated diffusion mechanisms, including (i) sliding by tracking and rotating along the DNA backbone, (ii) hopping via a series of microscopic protein–DNA dissociation and rebinding events, and (iii) intersegment transfer, in which a protein can move from one location to another via a looped intermediate.[[66–68](#ref66)] Individual molecules may stochastically interconvert between these states, leading to the large range of diffusion coefficients observed in these and prior studies.[[69–72](#ref69)] Additional studies will be required to define how Mlh1-Mlh3 diffusion on DNA facilitates its functions in both mismatch repair and meiotic recombination.[[40](#ref40)],[[62](#ref62)] Here, we conclude that wafer-based UV lithography can be used for fabricating universal microscope slides that support both single-stranded and double-stranded DNA curtains for high-throughput studies of protein–DNA interactions.
To further extend the utility of our wide-field surface patterning strategy, we integrated DNA curtains with a two-lane microfluidic device ([Figure 5](#fig5)). Multichannel microfluidic devices can be used to simultaneously observe enzyme function on different substrates or solution conditions.[[73–75](#ref73)] As a proof of principle, we exploited the large number of UV-patterned DNA curtain arrays to construct a dual-lane flowcell with two distinct DNA substrates in each of the two fluidically independent lanes ([Figure 5A](#fig5), bottom panel). Biotinylated lipid bilayers were deposited concurrently in both channels by flowing all reagents through the single flow port located at the bottom of the Y-shaped flowcell (Figure S4). The left lane was incubated with λ-DNA while the right lane was incubated with nucleosome-coated λ-DNA. The flowcell was mounted into the TIRF microscope, and both channels were rinsed with anti-Flag antibody conjugated QDs. The fluorescent antibody recognizes a 3xFlag epitope on histone H2A and is only expected to label nucleosome-containing DNA (lane 2). [Figure 5C](#fig5) demonstrates that we could readily image arrays of single-tethered DNA molecules in both channels, with only the right channel (lane 2) containing nucleosome-conjugated DNA. We anticipate that these flowcells will prove especially useful for studies that require side-by-side observation of protein behavior on different DNA substrates or to image protein activity under different buffer conditions (e.g., as a function of salt concentration or nucleotide state).

<figure class="paper-figure" id="fig5">
<img src="nihms731807f5.jpg" alt="Figure 5">
<figcaption><strong>Figure 5. A dual-lane flowcell for imaging two DNA substrates in the presence of buffer flow.</strong> (A) Cartoon schematic of the Y-shaped flowcell with two inlets and one outlet port. Each lane is 9 mm wide and separated by a 2 mm tape spacer (gray). Bottom panel: an image of yellow and blue food dye loaded into each of the two lanes. Scale bar: 5 mm. The lanes remain fluidically isolated for over 1 h. (B) Images captured from each lane during a single experiment. Lane 1 was assembled with λ-DNA, while lane 2 contained nucleosomecoated λ-DNA. Both channels were labeled with YOYO-1 DNA intercalating dye (Life Technologies). Nucleosomes were tagged with anti-FLAG QDs (magenta; 705 nm) and were exclusively observed in the right channel. Scale bar: 4 µm.</figcaption>
</figure>

---

## CONCLUSIONS
Here, we described a UV-lithography-based approach for rapidly creating arrays of DNA molecules on the surface of microfluidic flowcells. These universal slides support the assembly of both single- and double-tethered DNA molecules. Using this approach, we are able to rapidly pattern the entire surface of a quartz wafer without using EBL or other more specialized nanofabrication equipment. Furthermore, this method yields an order-of-magnitude increase in the density of tethered DNA molecules on the surface of each flowcell. Increasing the size of the field of view via a larger camera or a lower magnification objective can further increase the rate of data acquisition and multiple fields of view or additional flowcell lanes can be acquired by scanning a computer-controlled microscope stage. Additionally, we demonstrate that this approach is compatible with multichannel microfluidic flowcells for multiplexed single molecule imaging and manipulation.[[76](#ref76)] The method presented here will greatly facilitate single-molecule fluorescence studies of protein– nucleic acid interactions through the acquisition of large statistical data sets from individual experimental runs.

---
## ACKNOWLEDGMENTS
We thank Yoori Kim, Andrew A. Leal, and Armando de la Torre for constructs, purified proteins, and critical reading of this manuscript. This work was supported by the Cancer Prevention Research Institute of Texas (R1214 to I.J.F.), the Welch Foundation (F-l808 to I.J.F.), the National Institute of General Medical Sciences of the National Institutes of Health (GM53085 to E.A. and R00 GM097177 to I.J.F.), and the National Science Foundation (1453358 to I.J.F.). C.M.M. is funded by an NIH training grant (F32 GM112435). I.J.F. is a CPRIT Scholar in Cancer Research. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.
## ABBREVIATIONS 

AFM
    
atomic force microscopy 

CCD
    
charge coupled device 

Cr
    
chromium 

DIG
    
digoxigenin 

DNA
    
deoxyribonucleic acid 

dsDNA
    
double-stranded DNA 

EBL
    
electron beam lithography 

GFP
    
green fluorescence protein 

MSD
    
mean-squared displacement 

QD
    
quantum dot 

RCR
    
rolling circle replication 

RPA
    
replication protein A 

SLB
    
supported lipid bilayer 

ssDNA
    
single-stranded DNA 

std dev
    
standard deviation 

TIRF
    
total internal reflection fluorescence 

UV
    
ultraviolet.

## References

<span id="ref1">1.</span> Bustamante C, Smith SB, Liphardt J, Smith D. Single-Molecule Studies of DNA Mechanics. Curr. Opin. Struct. Biol. 2000;10:279–285. doi: 10.1016/s0959-440x(00)00085-3. [[DOI](https://doi.org/10.1016/s0959-440x\(00\)00085-3)]

<span id="ref2">2.</span> Bai L, Santangelo TJ, Wang MD. Single-Molecule Analysis of RNA Polymerase Transcription. Annu. Rev. Biophys. Biomol. Struct. 2006;35:343–360. doi: 10.1146/annurev.biophys.35.010406.150153. [[DOI](https://doi.org/10.1146/annurev.biophys.35.010406.150153)]

<span id="ref3">3.</span> Joo C, Balci H, Ishitsuka Y, Buranachai C, Ha T. Advances in Single-Molecule Fluorescence Methods for Molecular Biology. Annu. Rev. Biochem. 2008;77:51–76. doi: 10.1146/annurev.biochem.77.070606.101543. [[DOI](https://doi.org/10.1146/annurev.biochem.77.070606.101543)]

<span id="ref4">4.</span> Finkelstein IJ, Greene EC. Molecular Traffic Jams on DNA. Annu. Rev. Biophys. 2013;42:241–263. doi: 10.1146/annurev-biophys-083012-130304. [[DOI](https://doi.org/10.1146/annurev-biophys-083012-130304)]

<span id="ref5">5.</span> Stratmann SA, van Oijen AM. DNA Replication at the Single-Molecule Level. Chem. Soc. Rev. 2014;43:1201. doi: 10.1039/c3cs60391a. [[DOI](https://doi.org/10.1039/c3cs60391a)]

<span id="ref6">6.</span> Erie DA, Weninger KR. Single Molecule Studies of DNA Mismatch Repair. DNA Repair. 2014;20:71–81. doi: 10.1016/j.dnarep.2014.03.007. [[DOI](https://doi.org/10.1016/j.dnarep.2014.03.007)]

<span id="ref7">7.</span> Finkelstein IJ, Greene EC. Supported Lipid Bilayers and DNA Curtains for High-Throughput Single-Molecule Studies. Methods Mol. Biol. 2011;745:447–461. doi: 10.1007/978-1-61779-129-1_26. [[DOI](https://doi.org/10.1007/978-1-61779-129-1_26)]

<span id="ref8">8.</span> Robison AD, Finkelstein IJ. High-Throughput Single-Molecule Studies of Protein–DNA Interactions. FEBS Lett. 2014;588:3539–3546. doi: 10.1016/j.febslet.2014.05.021. [[DOI](https://doi.org/10.1016/j.febslet.2014.05.021)]

<span id="ref9">9.</span> Sternberg SH, Redding S, Jinek M, Greene EC, Doudna JA. DNA Interrogation by the CRISPR RNA-Guided Endonuclease Cas9. Nature. 2014;507:62–67. doi: 10.1038/nature13011. [[DOI](https://doi.org/10.1038/nature13011)]

<span id="ref10">10.</span> Finkelstein IJ, Visnapuu M-L, Greene EC. Single-Molecule Imaging Reveals Mechanisms of Protein Disruption by a DNA Translocase. Nature. 2010;468:983–987. doi: 10.1038/nature09561. [[DOI](https://doi.org/10.1038/nature09561)]

<span id="ref11">11.</span> Lee JY, Finkelstein IJ, Arciszewska LK, Sherratt DJ, Greene EC. Single-Molecule Imaging of FtsK Translocation Reveals Mechanistic Features of Protein-Protein Collisions on DNA. Mol. Cell. 2014;54:832–843. doi: 10.1016/j.molcel.2014.03.033. [[DOI](https://doi.org/10.1016/j.molcel.2014.03.033)]

<span id="ref12">12.</span> Castellana ET, Cremer PS. Solid Supported Lipid Bilayers: From Biophysical Studies to Sensor Design. Surf. Sci. Rep. 2006;61:429–444. doi: 10.1016/j.surfrep.2006.06.001. [[DOI](https://doi.org/10.1016/j.surfrep.2006.06.001)]

<span id="ref13">13.</span> Hafez IM, Ansell S, Cullis PR. Tunable pH-Sensitive Liposomes Composed of Mixtures of Cationic and Anionic Lipids. Biophys. J. 2000;79:1438–1446. doi: 10.1016/S0006-3495(00)76395-8. [[DOI](https://doi.org/10.1016/S0006-3495\(00\)76395-8)]

<span id="ref14">14.</span> Johansson B, Höök F, Klenerman D, Jönsson P. Label-Free Measurements of the Diffusivity of Molecules in Lipid Membranes. Chem Phys Chem. 2014;15:486–491. doi: 10.1002/cphc.201301136. [[DOI](https://doi.org/10.1002/cphc.201301136)]

<span id="ref15">15.</span> Wagner ML, Tamm LK. Tethered Polymer-Supported Planar Lipid Bilayers for Reconstitution of Integral Membrane Proteins: Silane-Polyethyleneglycol-Lipid as a Cushion and Covalent Linker. Biophys. J. 2000;79:1400–1414. doi: 10.1016/S0006-3495(00)76392-2. [[DOI](https://doi.org/10.1016/S0006-3495\(00\)76392-2)]

<span id="ref16">16.</span> Sackmann E. Supported Membranes: Scientific and Practical Applications. Science. 1996;271:43–48. doi: 10.1126/science.271.5245.43. [[DOI](https://doi.org/10.1126/science.271.5245.43)]

<span id="ref17">17.</span> Persson F, Fritzsche J, Mir KU, Modesti M, Westerlund F, Tegenfeldt JO. Lipid-Based Passivation in Nanofluidics. Nano Lett. 2012;12:2260–2265. doi: 10.1021/nl204535h. [[DOI](https://doi.org/10.1021/nl204535h)]

<span id="ref18">18.</span> Cremer PS, Boxer SG. Formation and Spreading of Lipid Bilayers on Planar Glass Supports. J. Phys. Chem. B. 1999;103:2554–2559.

<span id="ref19">19.</span> Feng ZV, Granick S, Gewirth AA. Modification of a Supported Lipid Bilayer by Polyelectrolyte Adsorption. Langmuir. 2004;20:8796–8804. doi: 10.1021/la049030w. [[DOI](https://doi.org/10.1021/la049030w)]

<span id="ref20">20.</span> Nakai K, Morigaki K, Iwasaki Y. Molecular Recognition on Fluidic Lipid Bilayer Microarray Corralled by Well-Defined Polymer Brushes. Soft Matter. 2010;6:5937–5943.

<span id="ref21">21.</span> Groves JT. Micropatterning Fluid Lipid Bilayers on Solid Supports. Science. 1997;275:651–653. doi: 10.1126/science.275.5300.651. [[DOI](https://doi.org/10.1126/science.275.5300.651)]

<span id="ref22">22.</span> Isono T, Ikeda T, Ogino T. Evolution of Supported Planar Lipid Bilayers on Step-Controlled Sapphire Surfaces. Langmuir. 2010;26:9607–9611. doi: 10.1021/la100179q. [[DOI](https://doi.org/10.1021/la100179q)]

<span id="ref23">23.</span> Groves JT, Boxer SG. Micropattern Formation in Supported Lipid Membranes. Acc. Chem. Res. 2002;35:149–157. doi: 10.1021/ar950039m. [[DOI](https://doi.org/10.1021/ar950039m)]

<span id="ref24">24.</span> Groves JT, Ulman N, Cremer PS, Boxer SG. Substrate– Membrane Interactions: Mechanisms for Imposing Patterns on a Fluid Bilayer Membrane. Langmuir. 1998;14:3347–3350.

<span id="ref25">25.</span> Groves JT, Kuriyan J. Molecular Mechanisms in Signal Transduction at the Membrane. Nat. Struct. Mol. Biol. 2010;17:659–665. doi: 10.1038/nsmb.1844. [[DOI](https://doi.org/10.1038/nsmb.1844)]

<span id="ref26">26.</span> Salafsky J, Groves JT, Boxer SG. Architecture and Function of Membrane Proteins in Planar Supported Bilayers: A Study with Photosynthetic Reaction Centers. Biochemistry. 1996;35:14773–14781. doi: 10.1021/bi961432i. [[DOI](https://doi.org/10.1021/bi961432i)]

<span id="ref27">27.</span> Kim P, Lee SE, Jung HS, Lee HY, Kawai T, Suh KY. Soft Lithographic Patterning of Supported Lipid Bilayers onto a Surface and inside Microfluidic Channels. Lab Chip. 2006;6:54–59. doi: 10.1039/b512593f. [[DOI](https://doi.org/10.1039/b512593f)]

<span id="ref28">28.</span> Hovis JS, Boxer SG. Patterning and Composition Arrays of Supported Lipid Bilayers by Microcontact Printing. Langmuir. 2001;17:3400–3405.

<span id="ref29">29.</span> Alom Ruiz S, Chen CS. Microcontact Printing: A Tool to Pattern. Soft Matter. 2007;3:168–177. doi: 10.1039/b613349e. [[DOI](https://doi.org/10.1039/b613349e)]

<span id="ref30">30.</span> Majd S, Mayer M. Hydrogel Stamping of Arrays of Supported Lipid Bilayers with Various Lipid Compositions for the Screening of Drug-Membrane and Protein-Membrane Interactions. Angew. Chem., Int. Ed. 2005;44:6697–6700. doi: 10.1002/anie.200502189. [[DOI](https://doi.org/10.1002/anie.200502189)]

<span id="ref31">31.</span> Xia Y, Whitesides GM. Soft Lithography. Annu. Rev. Mater. Sci. 1998;28:153–184.

<span id="ref32">32.</span> Gorman J, Fazio T, Wang F, Wind S, Greene EC. Nanofabricated Racks of Aligned and Anchored DNA Substrates for Single-Molecule Imaging. Langmuir. 2010;26:1372–1379. doi: 10.1021/la902443e. [[DOI](https://doi.org/10.1021/la902443e)]

<span id="ref33">33.</span> Visnapuu M-L, Fazio T, Wind S, Greene EC. Parallel Arrays of Geometric Nanowells for Assembling Curtains of DNA with Controlled Lateral Dispersion. Langmuir. 2008;24:11293–11299. doi: 10.1021/la8017634. [[DOI](https://doi.org/10.1021/la8017634)]

<span id="ref34">34.</span> Altissimo M. E-Beam Lithography for Micro-/nanofabrication. Biomicrofluidics. 2010;4:026503. doi: 10.1063/1.3437589. [[DOI](https://doi.org/10.1063/1.3437589)]

<span id="ref35">35.</span> Vieu C, Carcenac F, Pépin A, Chen Y, Mejias M, Lebib A, Manin-Ferlazzo L, Couraud L, Launois H. Electron Beam Lithography: Resolution Limits and Applications. Appl. Surf. Sci. 2000;164:111–117.

<span id="ref36">36.</span> Berkowski KL, Plunkett KN, Yu Q, Moore JS. Introduction to Photolithography: Preparation of Microscale Polymer Silhouettes. J. Chem. Educ. 2005;82:1365.

<span id="ref37">37.</span> Stevenson JTM, Gundlach AM. The Application of Photolithography to the Fabrication of Microcircuits. J. Phys. E: Sci. Instrum. 1986;19:654–667.

<span id="ref38">38.</span> Modesti M. Fluorescent Labeling of Proteins. Methods Mol. Biol. 2011;783:101–120. doi: 10.1007/978-1-61779-282-3_6. [[DOI](https://doi.org/10.1007/978-1-61779-282-3_6)]

<span id="ref39">39.</span> Gibb B, Silverstein TD, Finkelstein IJ, Greene EC. Single-Stranded DNA Curtains for Real-Time Single-Molecule Visualization of Protein-Nucleic Acid Interactions. Anal. Chem. 2012;84:7607–7612. doi: 10.1021/ac302117z. [[DOI](https://doi.org/10.1021/ac302117z)]

<span id="ref40">40.</span> Rogacheva MV, Manhart CM, Chen C, Guarne A, Surtees J, Alani E. Mlh1-Mlh3, A Meiotic Crossover and DNA Mismatch Repair Factor, Is a Msh2-Msh3-Stimulated Endonuclease. J. Biol. Chem. 2014;289:5664–5673. doi: 10.1074/jbc.M113.534644. [[DOI](https://doi.org/10.1074/jbc.M113.534644)]

<span id="ref41">41.</span> Thåström A, Lowary PT, Widom J. Measurement of Histone-DNA Interaction Free Energy in Nucleosomes. Methods. 2004;33:33–44. doi: 10.1016/j.ymeth.2003.10.018. [[DOI](https://doi.org/10.1016/j.ymeth.2003.10.018)]

<span id="ref42">42.</span> Luger K, Rechsteiner TJ, Richmond TJ. Preparation of Nucleosome Core Particle from Recombinant Histones. In: Paul M, Wassarman APW, editors. Methods in Enzymology. Vol. 304. New York: Academic Press; 1999. pp. 3–19. [[DOI](https://doi.org/10.1016/s0076-6879\(99\)04003-3)]

<span id="ref43">43.</span> Lee JY, Greene EC. Assembly of Recombinant Nucleosomes on Nanofabricated DNA Curtains for Single-Molecule Imaging. Methods Mol. Biol. 2011;778:243–258. doi: 10.1007/978-1-61779-261-8_16. [[DOI](https://doi.org/10.1007/978-1-61779-261-8_16)]

<span id="ref44">44.</span> Gorman J, Chowdhury A, Surtees JA, Shimada J, Reichman DR, Alani E, Greene EC. Dynamic Basis for One-Dimensional DNA Scanning by the Mismatch Repair Complex Msh2-Msh6. Mol. Cell. 2007;28:359–370. doi: 10.1016/j.molcel.2007.09.008. [[DOI](https://doi.org/10.1016/j.molcel.2007.09.008)]

<span id="ref45">45.</span> Meliorisz B, Partel S, Schnattinger T, Fühner T, Erdmann A, Hudek P. Investigation of High-Resolution Contact Printing. Microelectron. Eng. 2008;85:744–748.

<span id="ref46">46.</span> Kim J, Kim C, Allen MG, Yoon Y-K. Fabrication of 3D Nanostructures by Multidirectional UV Lithography and Predictive Structural Modeling. J. Micromech. Microeng. 2015;25:025017.

<span id="ref47">47.</span> Tero R, Watanabe H, Urisu T. Supported Phospholipid Bilayer Formation on Hydrophilicity-Controlled Silicon Dioxide Surfaces. Phys. Chem. Chem. Phys. 2006;8:3885. doi: 10.1039/b606052h. [[DOI](https://doi.org/10.1039/b606052h)]

<span id="ref48">48.</span> Zhuravlev LT. The Surface Chemistry of Amorphous Silica. Zhuravlev Model. Colloids Surf., A. 2000;173:1–38.

<span id="ref49">49.</span> Reimhult E, Kasemo B, Höök F. Rupture Pathway of Phosphatidylcholine Liposomes on Silicon Dioxide. Int. J. Mol. Sci. 2009;10:1683–1696. doi: 10.3390/ijms10041683. [[DOI](https://doi.org/10.3390/ijms10041683)]

<span id="ref50">50.</span> Gibb B, Ye LF, Gergoudis SC, Kwon Y, Niu H, Sung P, Greene EC. Concentration-Dependent Exchange of Replication Protein A on Single-Stranded DNA Revealed by Single-Molecule Imaging. PLoS One. 2014;9:e87922. doi: 10.1371/journal.pone.0087922. [[DOI](https://doi.org/10.1371/journal.pone.0087922)]

<span id="ref51">51.</span> Smith SB, Cui Y, Bustamante C. Overstretching B-DNA: The Elastic Response of Individual Double-Stranded and Single-Stranded DNA Molecules. Science. 1996;271:795–799. doi: 10.1126/science.271.5250.795. [[DOI](https://doi.org/10.1126/science.271.5250.795)]

<span id="ref52">52.</span> Lee JY, Wang F, Fazio T, Wind S, Greene EC. Measuring Intermolecular Rupture Forces with a Combined TIRF-Optical Trap Microscope and DNA Curtains. Biochem. Biophys. Res. Commun. 2012;426:565–570. doi: 10.1016/j.bbrc.2012.08.127. [[DOI](https://doi.org/10.1016/j.bbrc.2012.08.127)]

<span id="ref53">53.</span> Marrink SJ, Berger O, Tieleman P, Jähnig F. Adhesion Forces of Lipids in a Phospholipid Membrane Studied by Molecular Dynamics Simulations. Biophys. J. 1998;74:931–943. doi: 10.1016/S0006-3495(98)74016-0. [[DOI](https://doi.org/10.1016/S0006-3495\(98\)74016-0)]

<span id="ref54">54.</span> Evans E, Berk D, Leung A, Mohandas N. Detachment of Agglutinin-Bonded Red Blood Cells. II. Mechanical Energies to Separate Large Contact Areas. Biophys. J. 1991;59:849–860. doi: 10.1016/S0006-3495(91)82297-4. [[DOI](https://doi.org/10.1016/S0006-3495\(91\)82297-4)]

<span id="ref55">55.</span> Sitters G, Kamsma D, Thalhammer G, Ritsch-Marte M, Peterman EJG, Wuite GJL. Acoustic Force Spectroscopy. Nat. Methods. 2014;12:47–50. doi: 10.1038/nmeth.3183. [[DOI](https://doi.org/10.1038/nmeth.3183)]

<span id="ref56">56.</span> Chen G, Dubrawsky I, Mendez P, Georgiou G, Iverson BL. In Vitro Scanning Saturation Mutagenesis of All the Specificity Determining Residues in an Antibody Binding Site. Protein Eng., Des. Sel. 1999;12:349–356. doi: 10.1093/protein/12.4.349. [[DOI](https://doi.org/10.1093/protein/12.4.349)]

<span id="ref57">57.</span> Neuert G, Albrecht C, Pamir E, Gaub HE. Dynamic Force Spectroscopy of the Digoxigenin–antibody Complex. FEBS Lett. 2006;580:505–509. doi: 10.1016/j.febslet.2005.12.052. [[DOI](https://doi.org/10.1016/j.febslet.2005.12.052)]

<span id="ref58">58.</span> Strick TR, Allemand J-F, Bensimon D, Bensimon A, Croquette V. The Elasticity of a Single Supercoiled DNA Molecule. Science. 1996;271:1835–1837. doi: 10.1126/science.271.5257.1835. [[DOI](https://doi.org/10.1126/science.271.5257.1835)]

<span id="ref59">59.</span> Paik DH, Roskens VA, Perkins TT. Torsionally Constrained DNA for Single-Molecule Assays: An Efficient, Ligation-Free Method. Nucleic Acids Res. 2013;41:e179–e179. doi: 10.1093/nar/gkt699. [[DOI](https://doi.org/10.1093/nar/gkt699)]

<span id="ref60">60.</span> Seol Y, Neuman KC. Magnetic Tweezers for Single-Molecule Manipulation. Methods Mol. Biol. 2011;783:265–293. doi: 10.1007/978-1-61779-282-3_15. [[DOI](https://doi.org/10.1007/978-1-61779-282-3_15)]

<span id="ref61">61.</span> Flores-Rozas H, Kolodner RD. The Saccharomyces Cerevisiae MLH3 Gene Functions in MSH3-Dependent Suppression of Frameshift Mutations. Proc. Natl. Acad. Sci. U. S. A. 1998;95:12404–12409. doi: 10.1073/pnas.95.21.12404. [[DOI](https://doi.org/10.1073/pnas.95.21.12404)]

<span id="ref62">62.</span> Ranjha L, Anand R, Cejka P. The Saccharomyces Cerevisiae Mlh1-Mlh3 Heterodimer Is an Endonuclease That Preferentially Binds to Holliday Junctions. J. Biol. Chem. 2014;289:5674–5686. doi: 10.1074/jbc.M113.533810. [[DOI](https://doi.org/10.1074/jbc.M113.533810)]

<span id="ref63">63.</span> Plys AJ, Rogacheva MV, Greene EC, Alani E. The Unstructured Linker Arms of Mlh1–Pms1 Are Important for Interactions with DNA during Mismatch Repair. J. Mol. Biol. 2012;422:192–203. doi: 10.1016/j.jmb.2012.05.030. [[DOI](https://doi.org/10.1016/j.jmb.2012.05.030)]

<span id="ref64">64.</span> Gorman J, Wang F, Redding S, Plys AJ, Fazio T, Wind S, Alani EE, Greene EC. Single-Molecule Imaging Reveals Target-Search Mechanisms during DNA Mismatch Repair. Proc. Natl. Acad. Sci. U. S. A. 2012;109:E3074–E3083. doi: 10.1073/pnas.1211364109. [[DOI](https://doi.org/10.1073/pnas.1211364109)]

<span id="ref65">65.</span> Gorman J, Plys AJ, Visnapuu M-L, Alani E, Greene EC. Visualizing One-Dimensional Diffusion of Eukaryotic DNA Repair Factors along a Chromatin Lattice. Nat. Struct. Mol. Biol. 2010;17:932–938. doi: 10.1038/nsmb.1858. [[DOI](https://doi.org/10.1038/nsmb.1858)]

<span id="ref66">66.</span> Berg OG, Winter RB, von Hippel PH. Diffusion-Driven Mechanisms of Protein Translocation on Nucleic Acids. Biochemistry. 1981;20:6929–6948. doi: 10.1021/bi00527a028. [[DOI](https://doi.org/10.1021/bi00527a028)]

<span id="ref67">67.</span> Tafvizi A, Mirny LA, van Oijen AM. Dancing on DNA: Kinetic Aspects of Search Processes on DNA. Chem Phys Chem. 2011;12:1481–1489. doi: 10.1002/cphc.201100112. [[DOI](https://doi.org/10.1002/cphc.201100112)]

<span id="ref68">68.</span> Gorman J, Greene EC. Visualizing One-Dimensional Diffusion of Proteins along DNA. Nat. Struct. Mol. Biol. 2008;15:768–774. doi: 10.1038/nsmb.1441. [[DOI](https://doi.org/10.1038/nsmb.1441)]

<span id="ref69">69.</span> Blainey PC, Luo G, Kou SC, Mangel WF, Verdine GL, Bagchi B, Xie XS. Nonspecifically Bound Proteins Spin While Diffusing along DNA. Nat. Struct. Mol. Biol. 2009;16:1224–1229. doi: 10.1038/nsmb.1716. [[DOI](https://doi.org/10.1038/nsmb.1716)]

<span id="ref70">70.</span> Blainey PC, van Oijen AM, Banerjee A, Verdine GL, Xie XS. A Base-Excision DNA-Repair Protein Finds Intrahelical Lesion Bases by Fast Sliding in Contact with DNA. Proc. Natl. Acad. Sci. U. S. A. 2006;103:5752–5757. doi: 10.1073/pnas.0509723103. [[DOI](https://doi.org/10.1073/pnas.0509723103)]

<span id="ref71">71.</span> Lin J, Countryman P, Buncher N, Kaur P, E L, Zhang Y, Gibson G, You C, Watkins SC, Piehler J, et al. TRF1 and TRF2 Use Different Mechanisms to Find Telomeric DNA but Share a Novel Mechanism to Search for Protein Partners at Telomeres. Nucleic Acids Res. 2014;42:2493–2504. doi: 10.1093/nar/gkt1132. [[DOI](https://doi.org/10.1093/nar/gkt1132)]

<span id="ref72">72.</span> Kochaniak AB, Habuchi S, Loparo JJ, Chang DJ, Cimprich KA, Walter JC, van Oijen AM. Proliferating Cell Nuclear Antigen Uses Two Distinct Modes to Move along DNA. J. Biol. Chem. 2009;284:17700–17710. doi: 10.1074/jbc.M109.008706. [[DOI](https://doi.org/10.1074/jbc.M109.008706)]

<span id="ref73">73.</span> Brewer LR, Bianco PR. Laminar Flowcells for Single-Molecule Studies of DNA-Protein Interactions. Nat. Methods. 2008;5:517–525. doi: 10.1038/nmeth.1217. [[DOI](https://doi.org/10.1038/nmeth.1217)]

<span id="ref74">74.</span> Liu B, Baskin RJ, Kowalczykowski SC. DNA Unwinding Heterogeneity by RecBCD Results from Static Molecules Able to Equilibrate. Nature. 2013;500:482–485. doi: 10.1038/nature12333. [[DOI](https://doi.org/10.1038/nature12333)]

<span id="ref75">75.</span> Courson DS, Rock RS. Fast Benchtop Fabrication of Laminar Flow Chambers for Advanced Microscopy Techniques. PLoS One. 2009;4:e6479. doi: 10.1371/journal.pone.0006479. [[DOI](https://doi.org/10.1371/journal.pone.0006479)]

<span id="ref76">76.</span> Robison AD, Finkelstein IJ. Rapid Prototyping of Multichannel Microfluidic Devices for Single-Molecule DNA Curtain Imaging. Anal. Chem. 2014;86:4157–4163. doi: 10.1021/ac500267v. [[DOI](https://doi.org/10.1021/ac500267v)]


---

*Archived from [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC4624423/) on 2026-03-26.*
