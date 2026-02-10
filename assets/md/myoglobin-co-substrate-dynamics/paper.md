![](_page_0_Picture_1.jpeg)

# Myoglobin-CO Substate Structures and Dynamics: Multidimensional Vibrational Echoes and Molecular Dynamics **Simulations**

Kusai A. Merchant,† W. G. Noid,‡ Ryo Akiyama,‡ Ilya J. Finkelstein,† Alexei Goun,† Brian L. McClain, † Roger F. Loring, ‡ and M. D. Fayer\*, †

Contribution from the Department of Chemistry, Stanford University, Stanford, California 94305, and Department of Chemistry and Chemical Biology, Baker Laboratory, Cornell University, Ithaca, New York 14853

Received April 16, 2003; E-mail: faver@stanford.edu

Abstract: Spectrally resolved infrared stimulated vibrational echo data were obtained for sperm whale carbonmonoxymyoglobin (MbCO) at 300 K. The measured dephasing dynamics of the CO ligand are in agreement with dephasing dynamics calculated with molecular dynamics (MD) simulations for MbCO with the residue histidine-64 (His64) having its imidazole  $\epsilon$  nitrogen protonated (N $_{\epsilon}$ -H). The two conformational substate structures  $B_{\epsilon}$  and  $R_{\epsilon}$  observed in the MD simulations are assigned to the spectroscopic  $A_1$  and  $A_3$ conformational substates of MbCO, respectively, based on the agreement between the experimentally measured and calculated dephasing dynamics for these substates. In the A₁ substate, the N<sub>ϵ</sub>−H proton and  $N_{\delta}$  of His64 are approximately equidistant from the CO ligand, while in the  $A_3$  substate, the  $N_{\epsilon}-H$  of His64 is oriented toward the CO, and the N<sub>δ</sub> is on the surface of the protein. The MD simulations show that dynamics of His64 represent the major source of vibrational dephasing of the CO ligand in the A<sub>3</sub> state on both femtosecond and picosecond time scales. Dephasing in the A1 state is controlled by His64 on femtosecond time scales, and by the rest of the protein and the water solvent on longer time scales.

#### I. Introduction

Understanding protein dynamics is essential to establishing the relationships between protein structure and protein function. 1-5 Protein dynamics occur on a continuum of time scales, from the subpicosecond to the microsecond and longer. Such dynamics can be investigated with a variety of spectroscopic techniques. However, spectroscopic techniques with sufficient time resolution to probe the shortest time scale dynamics typically cannot provide the necessary structural specificity to assign these dynamics to particular atomic motions. Computational techniques such as molecular dynamics (MD) simulations can provide a view of protein motions at an atomic level of detail over a short range of time scales. The application of molecular simulation to interpret spectroscopic measurements requires the direct modeling of the experimental observable, as performed here.

Carbonmonoxymyoglobin (MbCO) (see Figure 1) has been extensively studied both experimentally6-19 and computationally.<sup>20–26</sup> Myoglobin (Mb) is a small globular heme protein

![](_page_0_Figure_17.jpeg)

Figure 1. Crystal structure of MbCO taken from the Protein Data Bank (1A6G). The heme group and three residues are indicated explicitly. The heme iron is covalently bound to the protein via His93. His64 is thought to play a major role in the conformational substates of the protein. Secondary structure is color-coded: helix A, blue; helix B, red; helix C, purple; helix D, green; helix E, orange; helix F, brown; helix G, pink; helix H, gray. All loops are colored cvan.

weighing approximately 17 kDa that is found in mammalian muscle tissue. The prosthetic heme group can reversibly bind a number of small molecule ligands such as O2, CO, and NO The crystal structure of Mb has been known for 40 years<sup>27</sup> and

<sup>†</sup> Stanford University.

<sup>&</sup>lt;sup>‡</sup> Cornell University

<sup>(1)</sup> Frauenfelder, H.; Sligar, S. G.; Wolynes, P. G. Science 1991, 254, 1598-1603

Hong, M. K.; Braunstein, D.; Cowen, B. R.; Frauenfelder, H.; Iben, I. E. T.; Mourant, J. R.; Ormos, P.; Scholl, R.; Schulte, A.; Steinbach, P. J.; Xie, A.; Young, R. D. *Biophys. J.* 1990, 58, 429–436.
 Andrews, B. K.; Romo, T.; Clarage, J. B.; Pettitt, B. M.; Phillips, G. N., Jr. Structure 1998, 6, 587–594.

Campbell, B. F.; Chance, M. R.; Friedman, J. M. Science 1987, 238, 373-

<sup>(5)</sup> Frauenfelder, H.; McMahon, B. H.; Austin, R. H.; Chu, K.; Groves, J. T. Proc. Natl. Acad. Sci. U.S.A. 2001, 98, 2370–2374.

has been continually refined over the last four decades to atomic resolution.<sup>28,29</sup> Because of its small size, relatively long MD simulations are tractable. 21,22 The CO stretching mode of MbCO has a strong transition dipole, making its infrared absorption an easily monitored experimental observable that can be used to track kinetics and dynamics in the protein. Studies on Mb, and in particular on MbCO, serve as tests for many of the ideas on the relationship between structure and function in proteins.

The infrared (IR) spectrum of the CO stretching mode of MbCO has at least three major absorption bands, 6,7,12-14 denoted  $A_0$  ( $\sim$ 1965 cm<sup>-1</sup>),  $A_1$  ( $\sim$ 1944 cm<sup>-1</sup>), and  $A_3$  ( $\sim$ 1932 cm<sup>-1</sup>). It is well known that these substates have different ligand binding rates, 1,6,13 but the nature of the structural differences between these substates is still in question. It has been suggested that different electrostatic environments in the heme pocket arising from different conformations of heme pocket residues are largely responsible for the observed bands. 15,19,25,26,30 Examples of previously hypothesized structures for the A substates are shown in Figure 2. Mutant studies have shown that the distal histidine, His64, plays a prominent role in determining the CO stretching frequency, 15,31 but the tautomerization and orientation of this residue remain unclear. His 64 has two titratable nitrogens,  $N_{\delta}$ and N<sub>e</sub>, either of which can be oriented toward the ligand through rotation of the imidazole ring. This residue is also fairly mobile and has been reported at a wide variety of distances (from 2 to 7 Å) from the CO ligand in crystal structures. 28,29,32 At low pH, His64 is thought to be doubly protonated and has been observed in a low pH crystal structure<sup>32</sup> and in a resonance Raman study<sup>11</sup> to be rotated out of the heme binding pocket

Caughey, W. S.; Shimada, H.; Choc, M. G.; Tucker, M. P. *Proc. Natl. Acad. Sci. U.S.A.* 1981, 78, 2903–2907.
 Rector, K. D.; Engholm, J. R.; Rella, C. W.; Hill, J. R.; Dlott, D. D.; Fayer, M. D. *J. Phys. Chem. A.* 1999, 103, 2381–2387.

M. D. J. Phys. Chem. A. 1999, 103, 2381-2367.
 Springer, B. A.; Sligar, S. G.; Olson, J. S.; Phillips, G. N., Jr. Chem. Rev. 1994, 94, 699-714.
 Tian, W. D.; Sage, J. T.; Champion, P. M.; Chien, E.; Sligar, S. G. Biochemistry 1996, 35, 3487-3502.
 Zhu, L.; Sage, J. T.; Rigos, A. A.; Morikis, D.; Champion, P. M. J. Mol. Biol. 1992, 224, 207-215.

Shimada, H.; Caughey, W. S. *J. Biol. Chem.* 1982, 257, 1893–1900.
 Johnson, J. B.; Lamb, D. C.; Frauenfelder, H.; Müller, J. D.; McMahon, B.; Nienhaus, G. U.; Young, R. D. *Biophys. J.* 1996, 71, 1563–1573.
 Müller, J. D.; McMahon, B. H.; Chen, E. Y. T.; Sligar, S. G.; Nienhaus, G. U. *Biophys. J.* 1999, 77, 1036–1051.

(15) Phillips, G. N., Jr.; Teodoro, M. L.; Li, T.; Smith, B.; Olson, J. S. J. Phys. Chem. B 1999, 103, 8817-8829.

(16) Fayer, M. D. Annu. Rev. Phys. Chem. 2001, 52, 315-356.

(17) Morikis, D.; Champion, P. M.; Springer, B. A.; Sligar, S. G. *Biochemistry* **1989**, 28, 4791-4800.

(18) Nienhaus, G. U.; Mourant, J. R.; Chu, K.; Frauenfelder, H. Biochemistry

(19) Oldfield, E.; Guo, K.; Augspurger, J. D.; Dykstra, C. E. J. Am. Chem. Soc. 1991, 113, 7537–7541.
(20) Rovira, C.; Schulze, B.; Eichinger, M.; Evanseck, J. D.; Parrinello, M. Biophys. J. 2001, 81, 435–445.

(21) Schulze, B. G.; Evanseck, J. D. J. Am. Chem. Soc. 1999, 121, 6444-6454.

(22) Meller, J.; Elber, R. *Biophys. J.* **1998**, 74, 789–802.
(23) Elber, R.; Karplus, M. *Science* **1987**, 235, 318–321

(24) Vitkup, D.; Ringe, D.; Petsko, G. A.; Karplus, M. *Nat. Struct. Biol.* **2000**, 7, 34–38.

(25) Kushkuley, B.; Stavrov, S. S. Biophys. J. 1996, 70, 1214–1229

(26) Kushkuley, B.; Stavrov, S. S. Biophys. J. 1997, 72, 899-912.
(27) Kendrew, J. C.; Dickerson, R. E.; Strandberg, B. E.; Hart, R. G.; Davies, D. R.; Phillips, D. C.; Shore, V. C. Nature 1960, 185, 422-427.
(28) Kachalova, G. S.; Popov, A. N.; Bartunik, H. D. Science 1999, 284, 473-

(29) Vojtechovsky, J.; Chu, K.; Berendzen, J.; Sweet, R. M.; Schlichting, I. *Biophys. J.* 1999, 77, 2153–2174.
(30) Franzen, S. *J. Am. Chem. Soc.* 2002, 124, 13271–13281.

(31) Li, T. S.; Quillin, M. L.; Phillips, G. N., Jr.; Olson, J. S. Biochemistry 1994 33 1433-1446

(32) Yang, F.; Phillips, G. N., Jr. J. Mol. Biol. 1996, 256, 762-774.

![](_page_1_Picture_30.jpeg)

Figure 2. Possible conformers and tautomers of His64 that have been assigned to conformational substates. (a)  $A_0$ . <sup>29,32</sup> The distal His64 is swung out of the pocket away from the ligand. The carbons of the imidazole side chain are labeled  $C_{\alpha}-C_{\gamma}$ . (b)  $A_1$ . <sup>19,20,29</sup> The  $N_{\epsilon}-H$  is in the pocket and oriented toward the ligand. (c)  $A_1$ . <sup>28,34</sup> The  $N_{\delta}-H$  is oriented toward the solvent, and the lone pairs of the  $N_{\epsilon}$  interact with the ligand. (d)  $A_3$ . <sup>29,45,80</sup> The  $N_{\epsilon}$ -H is in the pocket and is very close to and interacts strongly with the ligand. There may be a hydrogen bond between  $N_e$ -H and the CO. (e)  $A_1^{21,34}$  or  $A_3^{19}$  The  $N_\delta$ -H is in the pocket near the ligand. (f)  $A_1^{45}$  Both  $N_{\epsilon}$ -H and  $N_{\delta}$  are in the pocket. There is moderate interaction between His64 and the ligand.

away from the CO ligand in an "open" configuration. This conformer, with little interaction between His64 and the ligand, is thought to correspond to the A<sub>0</sub> substate, because at low pH the A<sub>0</sub> absorption line is the most intense. In addition, mutations of His64 to apolar residues produce a band at approximately the same frequency as the A<sub>0</sub> line.<sup>31</sup> At pH greater than 6, the A<sub>1</sub> and A<sub>3</sub> substates are the most populated at room temperature. 12,14 Kinetic hole burning studies on the MbCO A substates strongly suggest that the A<sub>1</sub> and A<sub>3</sub> substates are the result of a single tautomerization state of His64 because the time scale of interconversion between the  $A_1$  and  $A_3$  substates ( $\sim 1$  ns) is much faster than the time scale of His64 tautomerization (~1 μs). 13 Two recent atomic resolution crystal structures at neutral pH indicate that His64 is rotated into the heme pocket and is much closer to the ligand than in the A<sub>0</sub> substate, but the exact conformation of His64 remains uncertain. 28,29 In addition, these two crystal structures assign different tautomerization states to the singly protonated His64.

Both MD methods<sup>21,33</sup> and ab initio structural calculations<sup>20</sup> have been used to address the issue of the structural origins of the A substates, as well as the tautomerization state of His64.<sup>34</sup> Rovira et al.<sup>20</sup> performed mixed quantum mechanical/molecular mechanical calculations for various possible conformers for the A substates. On the basis of shifts of the CO vibrational frequency, they concluded that His64 exists as the N<sub>€</sub>-H tautomer with the proton pointed toward the ligand. However, they were unable to assign specific structures to the A<sub>1</sub> and A<sub>3</sub> substates. Other computational studies have proposed structural assignments for the A substates using the  $N_{\delta}$ -H tautomer, <sup>21,33</sup> which also reproduce the trends in the IR frequency shift. These studies illustrate that computations of CO vibrational frequencies alone cannot unambiguously identify the configurations associated with the spectroscopic substates.

In this paper, we present measured and calculated spectrally resolved infrared stimulated vibrational echo data on sperm

<sup>(6)</sup> Ansari, A.; Berendzen, J.; Braunstein, D.; Cowen, B. R.; Frauenfelder, H.; Hong, M. K.; Iben, I. E. T.; Johnson, J. B.; Ormos, P.; Sauke, T. B.; Scholl, R.; Schulte, A.; Steinbach, P. J.; Vittitow, J.; Young, R. D. *Biophys. Chem.* **1987**, *26*, 337–355.

<sup>(33)</sup> Schulze, B. G.; Grubmuller, H.; Evanseck, J. D. J. Am. Chem. Soc. 2000, 122 8700-8711

<sup>(34)</sup> Jewsbury, P.; Kitagawa, T. Biophys. J. 1994, 67, 2236-2250.

whale MbCO at 300 K. The ultrafast infrared vibrational echo<sup>8,35,36</sup> and the multidimensional vibrational echo<sup>37–46</sup> measure the fast structural dynamics of molecules through their effects on vibrational line shapes. The current work expands the findings from our previous report on horse heart MbCO<sup>40</sup> using a two-pulse spectrally resolved vibrational echo experiment. The three-pulse measurement (stimulated echo) permits the variation of the time delay  $T_{\rm w}$  between the second and third pulses, providing a probe of dynamics on longer time scales than possible with the two-pulse echo. The three-pulse vibrational echo provides a family of dynamical line shapes rather than the single dynamical line shape provided by a two-pulse vibrational echo. Therefore, a more rigorous comparison between the experiments and the calculations is made possible. More recently, we presented the results of a preliminary study<sup>45</sup> on horse heart MbCO using spectrally resolved stimulated echo measurements with a limited set of detection frequencies. Comparing these measurements on horse heart MbCO to MD simulations of sperm whale MbCO with the  $N_{\epsilon}$ -H tautomer of His64, we provisionally assigned the structural origins of the A<sub>1</sub> and A<sub>3</sub> substates of MbCO. Here, we present the spectrally resolved stimulated vibrational echo response at a wide range of detection frequencies for the substates of sperm whale MbCO. These measurements are compared to molecular dynamics results for sperm whale MbCO with both possible tautomerization states of His64. Using a time-dependent Stark effect model to derive a frequency-frequency correlation function (FFCF) for the CO ligand from the MD simulations, spectrally resolved stimulated vibrational echo spectra are computed from the FFCF for each tautomer and compared to the data.

The comparisons between the calculated vibrational echo data for the two His64 tautomers and the measured vibrational echo data over a wide range of frequency and  $T_{\rm w}$  indicate that the correct tautomer state of His64 is the N<sub>€</sub>-H structure and confirm the assignment of the structural origins of the A<sub>1</sub> and A<sub>3</sub> substates of MbCO made in our previous study.<sup>45</sup> In addition, analysis of the MD results reveals the origins of the dephasing dynamics for the A<sub>1</sub> and A<sub>3</sub> substates in terms of contributions from particular portions of the protein and the water solvent.

#### II. The Vibrational Echo

Time-dependent interactions between a vibrational mode and its environment give rise to spectral line broadening. The linear absorption spectrum of a vibrational spectroscopic transition

(35) Zimdars, D.; Tokmakoff, A.; Chen, S.; Greenfield, S. R.; Fayer, M. D.; Smith, T. I.; Schwettman, H. A. *Phys. Rev. Lett.* 1993, 70, 2718–2721.
(36) Tokmakoff, A.; Fayer, M. D. *Acc. Chem. Res.* 1995, 28, 437–445.
(37) Hamm, P.; Lim, M.; Hochstrasser, R. M. *Phys. Rev. Lett.* 1998, 81, 5326–

contains contributions from dynamics occurring on all time scales that are relevant to the interactions between the transition and its environment. In principle, all dynamical information about the interaction of a vibrational mode with its environment can be deduced from the absorption line shape alone.<sup>47</sup> In practice, however, dynamics on long time scales often dominate the shape of the linear absorption spectrum, masking the precise nature of the interactions between an oscillator and its environment.

The stimulated vibrational echo is a nonlinear spectroscopic technique capable of separating the dynamical processes contributing to an absorption spectrum line width by selectively eliminating the contribution of dynamics that have time scales slower than an experimentally controlled waiting time. 48-53 In a stimulated vibrational echo experiment, three resonant pulses with variable delay  $\tau$  between pulses 1 and 2 and variable delay  $T_{\rm w}$  between pulses 2 and 3 propagate along three different paths and are crossed in the sample. Interactions in the sample with the three applied pulses lead to the generation of a fourth vibrational echo pulse in a unique phase-matched direction. In a typical experiment, the value of  $T_{\rm w}$  is fixed, and the intensity of the vibrational echo signal is recorded as a function of the scanned time delay  $\tau$ . The stimulated vibrational echo eliminates spectral line broadening contributions from any dynamical processes that occur on time scales slower than the experimentally controlled time  $T_{\rm w}$ . <sup>48,49,51,52</sup> By measuring stimulated vibrational echoes decays for a series of  $T_{\rm w}$  times, the dynamical spectral broadening that occurs on different time scales is systematically mapped out. The stimulated vibrational echo thus probes the dynamics of the interaction of a vibrational mode and its environment. Thorough descriptions of the vibrational echo can be found in several recent reviews by Fayer and coworkers<sup>16,54</sup> and by Hamm and Hochstrasser.<sup>52</sup>

# III. Experimental and Computational Methods

A. Experimental Methods. The current experimental setup has been modified extensively from that reported previously. 16,40 An additional beam line for performing stimulated vibrational echoes has been added, as well as an array detector that greatly enhances the data acquisition rate. In the stimulated vibrational echo experiments reported here, an IR pulse (center frequency = 1940 cm<sup>-1</sup>, bandwidth = 125 cm<sup>-1</sup>, pulse duration = 125 fs) produced from a regeneratively amplified Ti: Sapphire pumped OPA (Spectra Physics) is beam split once, and each daughter pulse is split again with three 50%/50% (3.5-6.5  $\mu$ m) ZnSe beam splitters (II-VI Inc.) with broadband antireflection coating to produce four equal-energy pulses (~700 nJ), three of which are used in the experiments. The three pulses have wave vectors  $k_1$ ,  $k_2$ , and  $k_3$ with variable delay time  $\tau$  between the pulses with wave vector  $\vec{k}_1$  and  $k_2$  and with variable delay time  $T_{\rm w}$  between pulses with wave vector  $k_2$ 

<sup>(38)</sup> Merchant, K. A.; Thompson, D. E.; Fayer, M. D. Phys. Rev. Lett. 2001, 86, 3899-3902.

<sup>(39)</sup> Thompson, D. E.; Merchant, K. A.; Fayer, M. D. J. Chem. Phys. 2001, 115, 317–330.

<sup>(40)</sup> Merchant, K. A.; Thompson, D. E.; Xu, Q.-H.; Williams, R. B.; Loring, R. F.; Fayer, M. D. *Biophys. J.* **2002**, *82*, 3277–3288.

Golonzka, O.; Khalil, M.; Demirdoven, N.; Tokmakoff, A. Phys. Rev. Lett. **2001**, *86*, 2154–2157

<sup>(42)</sup> Golonzka, O.; Khalil, M.; Demirdoven, N.; Tokmakoff, A. J. Chem. Phys.

<sup>2001, 115, 10814-10828.
(43)</sup> Zanni, M. T.; Gnanakaran, S.; Stenger, J.; Hochstrasser, R. M. J. Phys. Chem. B 2001, 105, 6520-6535.

<sup>(44)</sup> Zanni, M. T.; Asplund, M. C.; Hochstrasser, R. M. J. Chem. Phys. 2001, *114*, 4579–4590.

<sup>(45)</sup> Merchant, K. A.; Noid, W. G.; Thompson, D. E.; Akiyama, R.; Loring, R. F.; Fayer, M. D. J. Phys. Chem. B 2003, 107, 4-7.

<sup>(46)</sup> Khalil, M.; Demirdoven, N.; Tokmakoff, A. Phys. Rev. Lett. 2003, 90, 047401(047404).

<sup>(47)</sup> Mukamel, S. Principles of Nonlinear Optical Spectroscopy; Oxford

 <sup>(47)</sup> Mikalinki, S. Thiches of Normalea Optical Specioscopy, Oxford University Press: New York, 1995.
 (48) Berg, M.; Walsh, C. A.; Narasimhan, L. R.; Littau, K. A.; Fayer, M. D. J. Chem. Phys. 1988, 88, 1564–1587.
 (49) Joo, T. H.; Jia, Y. W.; Yu, J. Y.; Lang, M. J.; Fleming, G. R. J. Chem.

Phys. 1996, 104, 6089-6108.

<sup>(50)</sup> de Boeij, W. P.; Pshenichnikov, M. S.; Wiersma, D. A. Chem. Phys. 1998, 233, 287–309.

Hamm, P.; Lim, M.; Hochstrasser, R. M. J. Phys. Chem. B 1998, 102, 6123 - 6138

<sup>(52)</sup> Hamm, P.; Hochstrasser, R. M. In Ultrafast Infrared and Raman Spectroscopy; Fayer, M. D., Ed.; Marcel Dekker: New York, 2001; Vol. 26,

<sup>(53)</sup> Asbury, J. B.; Steinel, T.; Stromberg, C.; Gaffney, K. J.; Piletic, I. R.; Goun, A.; Fayer, M. D. *Chem. Phys. Lett.* **2003**, *374*, 362–371.
(54) Merchant, K. A.; Xu, Q.-H.; Thompson, D. E.; Fayer, M. D. *J. Phys. Chem.* **4202**, 106, 2820, 2840.

A 2002, 106, 8839-8849.

and  $\vec{k}_3$ . The parent IR laser pulse was compressed by carefully balancing the amount of CaF<sub>2</sub> and Ge the beam passed through prior to being split. The beams were crossed and focused (spot size  $\sim 150~\mu m$ ) in the sample with a 6 in. focal length 90° gold coated off-axis parabolic reflector (Janos Technologies), and the vibrational echo signal was detected in the  $\vec{k}_s = \vec{k}_2 + \vec{k}_3 - \vec{k}_1$  phase-matched direction. Another off-axis parabolic reflector was used to collimate the emitted vibrational echo beam, and a HeNe laser beam was coaligned onto the vibrational echo beam to aid in further alignments and routing of the vibrational echo beam

The vibrational echo signal was dispersed in a SPEX 0.5 m monochromator (210 lines/mm) and detected with a 32-element HgCdTe array detector (Infrared Associates/Infrared Systems Development) with a resolution of  $\sim$ 1.2 cm<sup>-1</sup> per element. The data were recorded in blocks of 32 wavelengths by scanning  $\tau$  at a fixed value of  $T_{\rm w}$ , and then stepping the value of  $T_{\rm w}$ . Two blocks of 32 wavelengths were necessary to span the spectral range of the data. One pixel from adjacent frequency blocks was overlapped during the acquisition to ensure the consistency of the data. The frequency spectrum of the array was calibrated by comparing the spectrum of atmospheric water absorptions to data from the HITRAN96 molecular database. The response of each pixel was normalized to account for variations in the pixel signal output. The second pulse in the echo experiment was chopped at 500 Hz to permit subtraction of scattered light and to correct for drifts in the array detector baseline.

Recombinant sperm whale Mb in pH 8.0 Tris-chloride buffer ( $\sim$ 5 mg/mL) was obtained from Sigma. The solution was concentrated and flushed several times with 0.1 M phosphate pH 7 buffer (VWR Scientific) using a Microcon centrifugal filter device and was then concentrated to 15 mM. The sample was filtered with a 0.45  $\mu$ m cellulose acetate filter (Osmonics Laboratories) prior to the final concentration step. The Mb sample was reduced with excess sodium dithionite under a CO atmosphere. The sample was stirred under a CO atmosphere for an hour after reduction to ensure that all Mb had a CO ligand before being loaded into a 50  $\mu$ m gastight custom IR sample cell with 3 mm thick CaF<sub>2</sub> windows. Detailed power and concentration studies were performed, and the vibrational echo decay was found to be independent of both the laser intensity and the concentration used in the experiments.

**B. Molecular Dynamics Computations.** Molecular dynamics simulations at constant energy were performed using the MOIL software package<sup>55</sup> on one molecule of sperm whale MbCO, 2627 rigid water molecules, one  $SO_4^{2-}$  present in the crystal structure, and two Na<sup>+</sup> added to ensure electroneutrality,<sup>22</sup> at  $T \approx 300$  K. Simulations were run for both the N<sub>e</sub>-H and the N<sub>b</sub>-H tautomers of His64. Calculations for N<sub>b</sub>-H began with an equilibrated structure employed by Meller and Elber.<sup>22</sup> Treatment of the N<sub>e</sub>-H structure required modification of the original MOIL force field.<sup>56</sup> Dynamics reported here for the N<sub>e</sub>-H structure are determined from 39 production trajectories totaling 12.7

ns in duration. Dynamics for the  $N_{\delta}$ –H tautomer of His64 are calculated from 30 production trajectories totaling 12.0 ns in duration.

The CO transition frequency is highly sensitive to the electric field in the heme pocket. <sup>15,25,26,30,31</sup> Therefore, the pure dephasing dynamics in both tautomers of His64 were modeled as arising from time-dependent Stark effect perturbations of the transition frequency induced by the fluctuating electric field at the CO caused by protein and solvent motions. <sup>40,45,57</sup> The frequency fluctuations take the form

$$\delta\omega(t) = \lambda [\vec{u}(t) \cdot \vec{E}(t) - \langle \vec{u} \cdot \vec{E} \rangle] \tag{1}$$

where  $\vec{u}(t)$  is a unit vector along the electric dipole moment direction of CO,  $\vec{E}(t)$  is the instantaneous electric field at the midpoint of the CO bond, and  $\lambda$  is the Stark coupling constant, discussed further below. We calculated  $\vec{E}(t)$  at CO using Coulomb's law in a vacuum, the atomic partial charges in the MOIL force field, and the atomic positions generated by the MD. As described below, the spectrally resolved three-pulse vibrational echo signal and the linear absorption spectrum were calculated from the frequency—frequency correlation function (FFCF)

$$C(t) = \langle \delta\omega(t)\delta\omega(0)\rangle \tag{2}$$

The angular brackets in eqs 1 and 2 denote an equilibrium ensemble average.

**C. Vibrational Echo Computations.** We calculate the vibrational echo signal from third-order perturbation theory in the radiation—matter interaction. The third-order nonlinear polarization that generates the vibrational echo signal is a convolution of the material response function  $\sum_i R_i(t_3, t_2, t_1)$  with the applied optical fields  $E_i(t)$ :

$$P^{(3)}(\tau, T_{\mathbf{w}}, t) \propto \int_0^\infty dt_3 \int_0^\infty dt_2 \int_0^\infty dt_1 (\sum_i R_i(t_3, t_2, t_1)) \times E_3(t - t_3) E_2(T_{\mathbf{w}} + t - t_3 - t_2) E_1^*(\tau + T_{\mathbf{w}} + t - t_3 - t_2 - t_1)$$
(3)

The index i in eq 3 labels contributions to the response function within third-order perturbation theory,<sup>47</sup> which are described in Appendix A. The material system is modeled as a quantum-mechanical three-level system, coupled to a classical solvent that is treated within a second-order cumulant approximation. Details of the calculation of the nonlinear polarization  $P^{(3)}(\tau, T_{w}, t)$  are given in Appendix A.

The third-order nonlinear response function for MbCO is calculated by treating each of the conformational substates as a distinct species that retains its identity for the duration of the echo measurement. Each nonlinear response function is convolved with the temporal profiles of the excitation fields<sup>58</sup> as shown in eq 3 to yield the nonlinear polarization for that substate, and the total nonlinear polarization is computed from a concentration weighted sum of polarizations associated with each conformer

$$P_{\text{total}}^{(3)}(\tau, T_{\text{w}}, t) = \sum_{\alpha} c_{\alpha} P_{\alpha}^{(3)}(\tau, T_{\text{w}}, t)$$
 (4)

where  $c_{\alpha}$  is the concentration,  $P_{\alpha}^{(3)}$  is the nonlinear polarization, and  $\alpha$  is the index labeling the conformational substates. The transition dipole moment and anharmonicity were assumed to be the same for each substate. Determination of the concentrations  $c_{\alpha}$  is described in Section IVB and in Appendix B. The total nonlinear polarization was Fourier transformed with respect to the time variable t, and the power spectrum was computed as a function of the delay times  $\tau$  and  $T_{\rm w}$  and was evaluated at the detection frequencies for comparison with vibrational echo data. The linear absorption spectrum of the CO vibration is calculated within the same approximations used to calculate the nonlinear polarization by summing the concentration weighted contri-

<sup>(55)</sup> Elber, R.; Roitberg, A.; Simmerling, C.; Goldstein, R.; Li, H.; Verkhivker, G.; Keasar, C.; Zhang, J.; Ulitsky, A. Comput. Phys. Commun. 1994, 91, 159–189.

<sup>(56)</sup> MOIL (ref 55) defines force fields for two histidine structures: a neutral structure with the histidine protonated at N₀ and a singly charged structure with both N₀ and N₀ protonated. Simulating the N₀−H tautomer with MOIL required defining the associated force field parameters. MOIL derives atomic partial charges and Lennard-Jones parameters from the OPLS force field (Jorgensen; Tirado-Rives. J. Am. Chem. Soc. 1988, 110, 1666−1671), it obtains parameters describing bond lengths, bond angles, and torsional angles from the AMBER force field (Brooks; et al. J. Comput. Chem. 1983, 4, 187−217), and it obtains parameters describing improper torsional interactions from the CHARMM force field (Weiner; et al. J. Am. Chem. Soc. 1984, 106, 765−784). We obtained force field parameters for the N₀−H tautomer from the OPLS and AMBER force fields, for consistency with MOIL. An additional approximation was introduced in the case of the improper torsion interaction of Cρ₀, Cρ₀, C₀, and the unprotonated N₀. This interaction was approximated using the parameters for the improper torsion interaction of Cρ₀, Cρ₀, and the protonated N₀ of the doubly protonated histidine residue defined in MOIL. A complete listing of our modifications of MOIL force field files, which would allow our MD simulations to be reproduced, is given in the Supporting Information.

<sup>(57)</sup> Williams, R. B.; Loring, R. F.; Fayer, M. D. J. Phys. Chem. B 2001, 105, 4068–4071.

<sup>(58)</sup> The laser pulses in the calculation are transform-limited Gaussian line shape pulses with a full-width-half-maximum (fwhm) of 125 fs at the intensity level.

![](_page_4_Figure_1.jpeg)

**Figure 3.** Spectrally resolved stimulated vibrational echo signals for (a)  $T_{\rm w}=0$  ps and (b)  $T_{\rm w}=8$  ps. Slices through the vibrational echo decay data are shown in the main plots at frequencies 1946 cm<sup>-1</sup> (blue), 1938 cm<sup>-1</sup> (black), and 1930 cm<sup>-1</sup> (red). The full spectral response for the two  $T_{\rm w}$  values is shown in the inset, along with the frequencies of each slice. The maximum amplitude of each slice has been normalized for comparison. The vibrational echo decays are highly frequency dependent for early  $T_{\rm w}$ , but become independent of frequency for long  $T_{\rm w}$ . The trends shown in the data at these  $T_{\rm w}$  are representative of the trends seen in the full spectrally resolved vibrational echo data at other  $T_{\rm w}$ .

butions of each substate to the total linear polarization. The details of the calculation of the linear spectrum are presented in Appendix A.

## IV. Results and Discussion

A. Multidimensional Vibrational Echo Data. Multidimensional stimulated vibrational echo data are presented in Figure 3. Slices through the data at three frequencies and  $T_{\rm w}=0$ (Figure 3a) and 8 ps (Figure 3b) are shown in the main plots, while the full spectral response at these  $T_{\rm w}$  values is shown in the insets as  $\tau$ -frequency contour plots. Contour plots of the spectrally resolved stimulated vibrational echo signal on MbCO at other  $T_{\rm w}$  values can be found in the Supporting Information. It is clear from the data in Figure 3a that the measured vibrational echo decay is frequency dependent. The vibrational echo data around 1945 cm<sup>-1</sup> (blue curves) reflect contributions from the 0-1 transition of the  $A_1$  substate, while the vibrational echo data around 1932 cm<sup>-1</sup> (red curves) reflect contributions from the 0-1 transition of the  $A_3$  substate. The black curves show the echo decay for an intermediate frequency value of 1938 cm<sup>-1</sup>. The vibrational echo decay for the 1−2 transition of the  $A_1$  substate appears at  $\sim 1920$  cm<sup>-1</sup> (see insets) red-shifted from the 0-1 transition by the vibrational anharmonicity of the

CO stretching frequency,  $25.3 \text{ cm}^{-1}$ . The vibrational echo decay for the 1-2 transition of the  $A_3$  line appears to the red of the  $A_1$  1-2 transition at  $\sim 1910 \text{ cm}^{-1}$ . Because of the bandwidth and center frequency of the excitation pulses, the  $A_3$  1-2 transition is a small contribution to the data.

There are a number of significant qualitative features of the dependence of the spectrally resolved vibrational echo decays on  $\tau$ ,  $T_{\rm w}$ , and frequency. First, the vibrational echo decays faster around 1932 cm<sup>-1</sup> (red curves) than around 1945 cm<sup>-1</sup> (blue curves). Second, comparisons between Figure 3a and Figure 3b show that the difference between the vibrational echo decay dephasing dynamics at different frequencies decreases as  $T_{\rm w}$  is increased. The vibrational echo decays become more uniform as a function of frequency. Next, the vibrational echo signal decays faster as  $T_{\rm w}$  is increased, and the peak of the vibrational echo signal shifts to earlier time as  $T_{\rm w}$  is increased. These effects are the result of the inclusion of more dephasing processes in the  $T_{\rm w}$  period as  $T_{\rm w}$  is increased to encompass slower and slower dynamics. More dynamical broadening occurs as the system is allowed to evolve for longer and longer periods of time. Additional line broadening (frequency domain) results in a faster vibrational echo decay (time domain).

Our calculations of spectrally resolved stimulated vibrational echoes using the formalism of Appendix A reveal that these qualitative features are significantly influenced by the dynamics of the several overlapping vibrational transitions. However, the detailed shapes of the FFCFs used in the calculations control the quantitative agreement between the experimental data and calculated vibrational echo signal (see below). Several approaches have been previously proposed and applied to extract an FFCF directly from echo data on electronic and vibrational transitions. <sup>37,49,59</sup> Implementation of these strategies is problematic for MbCO, which is characterized by several overlapping transitions, none of which is massively inhomogeneously broadened. A calculation of relevant FFCFs from a molecular model, as described in the following section, is required to fully interpret spectrally resolved echo data for such a system.

B. Comparison of Measured and Simulated Dephasing **Dynamics from MD.** MD calculations of the instantaneous Stark shift  $\delta\omega(t)$  in eq 1 for the N<sub>e</sub>-H structure show pronounced two-state behavior with a state  $R_{\epsilon}$  characterized by a redder CO vibrational frequency and a state  $B_{\epsilon}$  characterized by a bluer CO vibrational frequency. The Stark shifts of these two states fluctuate about mean values that differ by  $9.3\lambda$  in units of cm<sup>-1</sup>, where  $\lambda$  is the value of the Stark coupling constant expressed in units of cm<sup>-1</sup>/(MV/cm). In 13 trajectories of the 39 production trajectories of the  $N_{\epsilon}$ -H tautomer, the system began and ended in the state  $R_{\epsilon}$  without making a transition to the  $B_{\epsilon}$  state, and in 3 trajectories, MbCO began and ended in  $B_{\epsilon}$  without making a transition to  $R_{\epsilon}$ . In total, the  $R_{\epsilon}$  state was observed 47 times for 8.96 ns of simulation. The  $B_{\epsilon}$  state was observed 30 times for 3.24 ns of simulation. The time duration of a transition between the two conformers was ~500 fs. From this limited number of jumps, the average substate lifetimes of  $R_{\epsilon}$  and  $B_{\epsilon}$  are on the order of 100–200 ps. The limited time scale of the simulation prevents us from assigning quantitatively correct lifetimes or statistical weights to the R<sub>e</sub> and B<sub>e</sub> states. However, the lifetimes of the states are not required for the

![](_page_5_Figure_2.jpeg)

Figure 4. An example of a MD trajectory showing the transition between the  $R_\epsilon$  state and the  $B_\epsilon$  state. A transition occurs from  $R_\epsilon$  to  $B_\epsilon$  at  ${\sim}280$  ps, and then back to the  $R_\epsilon$  state at  ${\sim}345$  ps. (a) The average value of the Stark frequency shift changes abruptly during the transition. (b) The distance between  $N_\epsilon{-}H$  (black) and  $N_\delta$  of His64 (red) during the trajectory. In the  $R_\epsilon$  state,  $N_\epsilon{-}H$  is much closer to the ligand than  $N_\delta$ . In the  $B_\epsilon$  state, the distances of  $N_\epsilon{-}H$  and  $N_\delta$  of His64 to the CO are about the same. (c) The dihedral angle of the  $C_\beta{-}C_\delta$  bond changes during the transition from  $R_\epsilon$  to  $B_\epsilon$  at  ${\sim}280$  ps and then back at  ${\sim}345$  ps.

analysis presented below. A representative trajectory of  $\delta\omega(t)$  of duration 200 ps showing both states is plotted in Figure 4a.

The change in the CO vibrational frequency shown in Figure 4a is associated with the motion of the distal histidine, His64, between two well-defined configurations. Figure 4b shows the fluctuating distance between the  $N_{\epsilon}$ -H proton and the midpoint of the CO bond (black) and the fluctuating distance between  $N_{\delta}$  and the CO (red) for the same MD trajectory depicted in Figure 4a. In state  $R_{\epsilon}$ , the  $N_{\epsilon}$ -H bond points toward the CO ligand with a mean distance from H to CO midpoint of 3.2 Å. The mean distance from  $N_{\delta}$  to CO is 5.8 Å. In the  $B_{\epsilon}$  state, His64 has rotated about the  $C_{\beta}$ - $C_{\gamma}$  bond relative to the  $R_{\epsilon}$  state, such that both the  $N_{\epsilon}$  proton and the  $N_{\delta}$  are approximately the same distance from the ligand, with mean distances of 4.6 and

**Table 1.** Coordinates for Heme Pocket Atoms for the  $R_{\varepsilon}$  and  $B_{\varepsilon}$  Configurations

|                                     | distance (Å)         |                      | variance (Å) <sup>2</sup> |                       |
|-------------------------------------|----------------------|----------------------|---------------------------|-----------------------|
|                                     | $R_{\epsilon}$ state | $B_{\epsilon}$ state | $R_{\epsilon}$ state      | $B_{\epsilon}$ state  |
| $R(N_{\delta}-O)$ (His64)           | 5.69                 | 4.46                 | 0.205                     | 0.142                 |
| $R(HN_{\epsilon}-O)$ (His64)        | 3.07                 | 4.63                 | 0.300                     | 0.618                 |
| R(C-O)                              | 1.13                 | 1.13                 | 0.000                     | 0.000                 |
| R(Fe-C)                             | 1.90                 | 1.90                 | 0.001                     | 0.001                 |
| $R(Fe-N_a)$ (Heme)                  | 1.97                 | 1.97                 | 0.001                     | 0.001                 |
| $R(Fe-N_b)$                         | 1.97                 | 1.97                 | 0.001                     | 0.001                 |
| $R(Fe-N_c)$                         | 1.97                 | 1.97                 | 0.001                     | 0.001                 |
| $R(Fe-N_d)$                         | 1.97                 | 1.97                 | 0.001                     | 0.001                 |
| $R(\text{Fe-N}_{\epsilon})$ (His93) | 2.21                 | 2.21                 | 0.004                     | 0.004                 |
|                                     | angle                | angle                | $R_{\epsilon}$ state      | $B_{\epsilon}$ state  |
|                                     | (deg)                | (deg)                | ((deg)2)                  | ((deg) <sup>2</sup> ) |
| (Fe-C-O)                            | 173.38               | 173.33               | 11.97                     | 12.20                 |

4.8 Å, respectively. The angle relevant to this rotation is that between the plane formed by  $C_{\alpha}$ ,  $C_{\beta}$ , and  $C_{\gamma}$  of the histidine arm, and the plane formed by  $C_{\gamma}$ ,  $C_{\delta}$ , and  $N_{\delta}$  of the imidazole ring. The labeling of the carbon atoms of the histidine arm is defined in Figure 2a. The time dependence of this dihedral angle for the trajectory of Figure 4a and 4b is shown in Figure 4c. This angle rotates from a mean value of  $108^{\circ}$  in  $R_{\epsilon}$  to a mean value of  $68^{\circ}$  in  $B_{\epsilon}$ . In the  $B_{\epsilon}$  state, the  $N_{\epsilon}$ -H bond is not oriented directly toward the ligand but rather toward the heme, and both  $N_{\epsilon}$ -H and  $N_{\delta}$  are in the interior of the protein. The state  $R_{\epsilon}$  has a structure qualitatively similar to Figure 2b, while  $B_{\epsilon}$  qualitatively resembles Figure 2f. Table 1 summarizes some of the geometric differences between the  $B_{\epsilon}$  and  $R_{\epsilon}$  states. Representative snapshots of the  $R_{\epsilon}$  and  $R_{\epsilon}$  configurations are shown in Figure 5a and 5b, respectively.

Frequency—frequency correlation functions were calculated for the two substates from eqs 1 and 2 and are shown in Figure 6a by the red  $(R_{\epsilon})$  and blue  $(B_{\epsilon})$  curves. The FFCF for  $R_{\epsilon}$  has a larger initial amplitude than that for  $B_{\epsilon}$ , indicating a larger root-mean-squared Stark shift fluctuation for the former state, which may also be seen qualitatively from the frequency fluctuations in Figure 4a. The FFCF for  $R_{\epsilon}$  has an initial rapid decay on the time scale of  $\sim 100$  fs, followed by slower decay on the picosecond time scale. This FFCF shows pronounced ringing during the first few picoseconds. The  $B_{\epsilon}$  state FFCF, while of smaller initial amplitude, shows similar rapid and slower decays, but does not display the fine structure of the FFCF for  $R_{\epsilon}$ . Neither FFCF is well described as a sum of two exponential decays.

The FFCFs for the  $R_{\epsilon}$  and  $B_{\epsilon}$  states were used to compute spectrally resolved vibrational echo decays for particular values of  $T_{\rm w}$ . The IR line shape of MbCO shows two dominant features: the redder  $A_3$  peak at  $\sim 1934$  cm<sup>-1</sup> and the bluer  $A_1$  peak at 1945 cm<sup>-1</sup>. The  $R_{\epsilon}$  state FFCF was used to model the dynamics of the  $A_3$  substate, and the  $B_{\epsilon}$  state FFCF was used to model the dynamics of the  $A_1$  substate. We assumed that the simulation did not show the  $A_0$  substate, because His64 never adopted a swung out configuration seen in low pH crystal structures.<sup>32</sup> Also, the inverse rate constant for interconversion between the  $A_1$  and  $A_3$  substates has been estimated to be  $\sim 1$  ns, while the inverse rate constant for interchanging between the  $A_1$  and  $A_0$  substates is  $\sim 1$   $\mu s$ .<sup>10,13</sup> Transitions between the  $R_{\epsilon}$  and  $R_{\epsilon}$  states occurred numerous times during the 12.8 ns of

![](_page_6_Picture_1.jpeg)

![](_page_6_Picture_2.jpeg)

**Figure 5.** Snapshots of the heme pocket<sup>45</sup> during the MD trajectory shown in Figure 4. (a) The  $R_{\epsilon}$  configuration has  $N_{\epsilon}$ —H oriented toward the CO, and the  $N_{\delta}$  oriented toward the solvent. (b) In the  $B_{\epsilon}$  configuration, the imidazole ring of His64 has undergone a rotation around the  $C_{\beta}$ — $C_{\delta}$  bond so that  $N_{\epsilon}$ —H is oriented away from the CO ligand and  $N_{\delta}$  is inside the heme pocket.

MD simulations, consistent with the rate constant between  $A_1$  and  $A_3$ .

Calculation of the spectrally resolved stimulated vibrational echo decay curves from the formalism of section III requires knowledge of the following quantities: the peak frequencies of the substates, the concentrations of the substates ( $c_{\alpha}$  in eq 4), the vibrational lifetimes of each substate, and the Stark coupling constant  $\lambda$  in eq 1. We include all three A substate peaks to reproduce the features seen in the data. The approximate inclusion of the A<sub>0</sub> state, not observed in the simulation, is described in Appendix B. The line center for the A<sub>1</sub> substate was measured by taking a vibrational echo spectrum at  $\tau = 3.0$  ps,  $T_{\rm w} = 0.25$  ps, shown in Figure 7. At this value of  $\tau$ , vibrational echo contributions from the  $A_3$  substate are negligible, leaving only the 0-1 and 1-2 transition peaks of the A<sub>1</sub> substate. The vibrational echo spectrum in Figure 7 is an example of vibrational echo peak suppression, where differences in dephasing times are used as a means of enhancing certain peaks relative to other peaks. 60,61 Further details used

![](_page_6_Figure_8.jpeg)

Figure 6. Frequency–frequency correlation functions (FFCFs) for the two tautomers of MbCO derived from MD simulations used to calculate vibrational echo signals. (a) The N<sub>ε</sub>–H tautomer of His64. The R<sub>ε</sub> conformer (red) and B<sub>ε</sub> conformer (blue) both have a fast initial decay over the first few picoseconds, and then continue to decay slowly. The R<sub>ε</sub> substate has a much larger initial amplitude. The value of the Stark coupling constant  $\lambda$  is  $\lambda = 2.1$  cm<sup>-1</sup>/(MV/cm). (b) The N<sub>δ</sub>–H tautomer of His64. The B<sub>δ</sub> conformer (blue) has a larger initial amplitude than the R<sub>δ</sub> (red) conformer. The value of  $\lambda$  is  $\lambda = 1.4$  cm<sup>-1</sup>/(MV/cm).

in the calculation of the spectrally resolved vibrational echo data for the A substates are presented in Appendix B. However, it is important to note that the substate concentrations,  $c_{\alpha}$  in eq 4, and center line frequencies are determined by fitting the linear absorption spectrum to Voigt profiles. Therefore, the determination of the center frequencies and concentrations does not depend on any of the MD simulations used to analyze the stimulated vibrational echo data. The same line center frequencies and substate concentrations are used in the comparisons of the MD simulations for the two tautomers. All parameter values employed in the linear spectrum and vibrational echo calculations are summarized in Table 2.

Measured vibrational echo decays for four frequencies and three values of  $T_{\rm w}$  are shown in Figure 8 in black. The red curves show vibrational echoes calculated using FFCFs for the N<sub>e</sub>-H tautomer. The FFCFs calculated from the MD simulations can be used to fit the experimental vibrational echo data for all measured values of  $T_{\rm w}$ . In the fits, there is only one adjustable parameter, the Stark coupling constant,  $\lambda$ . The best fit value for the Stark coupling constant was found to be  $\lambda$ 

<sup>(60)</sup> Rector, K. D.; Zimdars, D. A.; Fayer, M. D. J. Chem. Phys. 1998, 109, 5455–5465.

<sup>(61)</sup> Rector, K. D.; Fayer, M. D.; Engholm, J. R.; Crosson, E.; Smith, T. I.; Schwettmann, H. A. *Chem. Phys. Lett.* **1999**, *305*, 51–56.

![](_page_7_Figure_2.jpeg)

**Figure 7.** Vibrational echo spectrum at  $\tau = 2.1$  ps,  $T_{\rm w} = 0$  ps. The 0-1 and 1-2 transitions of the A<sub>1</sub> substate are clearly seen at 1945 and 1920 cm<sup>-1</sup>. Contributions to the echo spectrum from the A<sub>3</sub> substate have been eliminated using T<sub>2</sub> selectivity. The splitting between the two peaks gives an anharmonicity of  $\Delta = 25.3 \text{ cm}^{-1}$ 

Table 2. Summary of Parameters Used in Vibrational Echo Calculations<sup>a</sup>

| MbCO<br>substate                                   | center<br>frequency<br>(cm <sup>-1</sup> ) | concentration<br>(relative) | lifetime<br>(ps)     | FFCF $(N_{\epsilon}-H$ tautomer)                                                        | FFCF ( $N_{\delta}$ —H tautomer)                                                  |
|----------------------------------------------------|--------------------------------------------|-----------------------------|----------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| A <sub>0</sub><br>A <sub>1</sub><br>A <sub>3</sub> | 1965<br>1945<br>1934                       | 0.125<br>1.4<br>1           | 16.5<br>16.5<br>14.7 | $\begin{array}{c} 0.64 \times B_{\epsilon} \\ B_{\epsilon} \\ R_{\epsilon} \end{array}$ | $\begin{array}{c} 0.64 \times B_{\delta} \\ B_{\delta} \\ R_{\delta} \end{array}$ |

<sup>a</sup> The transition dipole moments for all A substates are assumed to be the same. An anharmonicity of  $\Delta = 25.4 \text{ cm}^{-1}$  is assumed for all transitions. The vibrational lifetimes for the A<sub>1</sub> and A<sub>3</sub> substates have been measured previously, 40 and the lifetime of the A<sub>0</sub> substate is assumed to be the same as the lifetime of the  $A_1$  substate. The laser pulse is assumed to be a transform-limited Gaussian pulse centered at 1940 cm<sup>-1</sup> with a fwhm = 125 fs. The FFCFs for the  $\hat{N}_{\epsilon}$ -H tautomer were used in the calculations shown in Figures 8 and 9, and the FFCFs for the  $N_{\delta}$ -H tautomer were used in the calculations shown in Figures 10 and 11. See Appendix B for further details.

2.1 cm<sup>-1</sup>/(MV/cm).<sup>63</sup> The value for  $\lambda$  has been determined experimentally by Boxer and co-workers using vibrational Stark spectroscopy on MbCO and a number of other heme-CO systems. 64,65 They found the Stark coupling constant to be  $\lambda =$  $1.8-2.2~\text{cm}^{-1}/(\text{MV/cm})$ . 66 Our value of  $\lambda$  is in excellent agreement with these results. Thus, the only adjustable parameter in the fit of the experimental data using the FFCF determined by the MD simulations is, within experimental error, the same as the measured value. Spectrally resolved stimulated vibrational echo decays are very sensitive to protein structure and dynamics. The agreement between experiment and theory provides strong support for the assignment of the  $A_1$  and  $A_3$  structures.

Figure 9 displays the measured linear absorption spectrum (solid curve) and the calculated linear spectrum (dashed curve) employing the same parameter values used for the calculated

(62) At large values of  $T_{\rm w}$ , an additional small signal around  $\tau = 0$  is observed. This signal is due to a nonresonant contribution from the solvent background that results from the breaking of hydrogen bonds in the solvent. Correcting the vibrational echo data to remove this signal contribution gives agreement between the calculated and measured signals at large values of  $T_{\rm w}$ 

comparable to the agreement shown in Figure 8. (63) The best fit value of  $\lambda$  for MbCO at 300 K was previously reported as  $\lambda$ = 1.9 cm<sup>-1</sup>/(MV/cm) (ref 45). The vibrational echo decay at the concentrations used in those experiments was concentration-dependent and became faster as the concentration was reduced. We attribute the slower vibrational echo decays in ref 45 to the higher viscosity of the more

concentrated protein sample.
(64) Park, E. S.; Boxer, S. G. J. Phys. Chem. B **2002**, 106, 5800-5806.
(65) Park, E. S.; Boxer, S. G. J. Phys. Chem. B **2002**, 106, 8910-8910.

vibrational echo decays in Figure 8, and listed in Table 2. The center frequencies and relative substate concentrations derived from the model independent fits to the linear spectrum are used and are not adjustable parameters. The simulated linear spectrum is slightly wider than the measured line shape, and the amplitude of the A<sub>0</sub> peak is too large. Overall, the agreement with the linear spectrum is reasonably good. However, the MD results overestimate the splitting between the A<sub>1</sub> and A<sub>3</sub> substates by  $\sim$ 8 cm<sup>-1</sup>, predicting a splitting of 19 cm<sup>-1</sup> between the substates. While the stimulated vibrational echo is only sensitive to dynamics on short time scales, the linear absorption spectrum is also sensitive to dynamics on all possible time scales. Very long time scale dynamics may not be accurately modeled using only  $\sim$ 13 ns of MD simulation. Nonetheless, the linear spectrum agrees reasonably well and shows, along with the dynamical calculations in Figure 8, that the simulated FFCFs for the  $N_{\epsilon}$ -H tautomer are consistent with the measured dynamics of the A<sub>1</sub> and  $A_3$  substates of MbCO.

Trajectories of the fluctuating CO Stark shift for the  $N_{\delta}$ -H structure, analogous to the calculation for N<sub>e</sub>−H shown in Figure 4a, also show pronounced two-state behavior, with a blue state  $B_{\delta}$  (qualitatively similar to Figure 2c) and a red state  $R_{\delta}$ (qualitatively similar to Figure 2e) having vibrational frequencies separated by 18.1  $\lambda$  in units of cm<sup>-1</sup>.67 The state B<sub> $\delta$ </sub> has a structure similar to  $R_{\epsilon}$ . In both structures,  $N_{\epsilon}$  points in the heme pocket toward the CO ligand. However, whereas in  $R_{\epsilon}$  the proton is directed toward the ligand, in  $B_{\delta}$  the proton is on the surface of the protein and directed into the solvent. The mean dihedral angle defined for Figure 4b has the same value of  $108^{\circ}$  for  $B_{\delta}$ as for  $R_{\epsilon}$ . In  $B_{\delta}$ , the distances from  $N_{\epsilon}$  and the  $N_{\delta}-H$  proton to the midpoint of the CO bond are 5.6 and 9.5 Å, respectively. The red state  $R_{\delta}$  is structurally similar to  $B_{\epsilon}$ , but with the imidazole proton directed into the heme pocket, and with a mean dihedral angle of  $80^{\circ}$ , as compared to  $68^{\circ}$  for  $B_{\epsilon}$ . The mean distances from  $N_{\epsilon}$  and the  $N_{\delta}$ -H proton to the midpoint of the CO bond for the  $R_{\delta}$  structure are 7.2 and 6.5 Å, respectively.

The FFCFs associated with these states are shown in Figure 6b. The FFCF for  $B_{\delta}$  resembles that for  $R_{\epsilon}$  in having a relatively large initial value and in displaying ringing on the picosecond time scale. Similarly, the FFCF for  $R_{\delta}$  resembles that for  $B_{\epsilon}$  in having a relatively small initial value and lacking fine structure. These FFCFs were used to compute the vibrational echo decays and absorption line shape with the same procedure, line centers, and concentrations used for the  $N_{\epsilon}$ -H calculation. Details of the fitting procedure are in Appendix B.

The computed vibrational echo signal for the  $N_{\delta}$ -H tautomer is shown in Figure 10 for the same frequencies and values of  $T_{\rm w}$  as shown in Figure 8. The calculated linear spectrum (dashed curve) using the FFCFs for the  $N_{\delta}$ -H tautomer is compared to the experimental linear spectrum for sperm whale MbCO (solid

(66) The range in the value of  $\lambda$  results from uncertainties in the local electric field correction factor for the heme pocket associated with applying an external electric field to a dielectric medium. See refs 64-65.

Our first reported echo calculations for MbCO (refs 40 and 57) were based on simulations of the N<sub>0</sub>−H structure. In those simulations, we adopted a criterion suggested by Schulze and Evanseck (ref 21) and associated with the A<sub>0</sub> state all structures in which the distance between the midpoint of the CO bond and the proton of N<sub>δ</sub>-H exceeds 6.5 Å. Such structures were not investigated in those calculations. We have therefore performed new simulations of MbCO with the No-H tautomer of His64 to examine the FFCFs associated with all spectroscopically distinct substates generated in the simulation. In addition, we have corrected an error in our previous calculations for the N<sub>δ</sub>-H tautomer of the electric field at the CO generated by the solvent.

![](_page_8_Figure_1.jpeg)

Figure 8. Comparison of the measured vibrational echo data (black) with the calculated vibrational echo data (red) for the  $N_{\epsilon}$ -H tautomer of His64. The vibrational echo signals were calculated using the FFCFs shown in Figure 6a. The parameters used in the vibrational echo calculation are listed in Table 2. Spectrally resolved vibrational echo decays are shown for the frequencies 1930, 1935, 1940, and 1945 cm<sup>-1</sup>, and  $T_{\rm w}=0$  ps (a-d), 2 ps (e-h), and 8 ps (i-l). Vibrational echo decays for a particular frequency as a function of  $T_{\rm w}$  are in columns. The oscillations in the echo decays in panels c and d are due to anharmonic accidental degeneracy beats<sup>38,77,81</sup> between the 0-1 transition of the  $A_1$  line and the 1-2 transition of the  $A_0$  line.

 $\it Table~3.~$  Stark Effect Dephasing Contributions from MD Simulations  $\it ^a$ 

|                                    | $R_{\epsilon}$ state                            |                              | $B_{\epsilon}$ state                            |                              |
|------------------------------------|-------------------------------------------------|------------------------------|-------------------------------------------------|------------------------------|
|                                    | Stark<br>frequency<br>shift (cm <sup>-1</sup> ) | FFCF $(t=0)$ $((rad/ps)^2)$  | Stark<br>frequency<br>shift (cm <sup>-1</sup> ) | FFCF $(t=0)$ $((rad/ps)^2)$  |
| all<br>protein<br>His64<br>solvent | -48.8<br>-51.7<br>-6.7<br>2.8                   | 9.35<br>8.45<br>7.75<br>2.01 | -29.6<br>-31.4<br>14.0<br>1.8                   | 2.80<br>2.12<br>1.03<br>1.93 |

 $^a$  The Stark effect frequency shift contributions and initial amplitudes of the FFCFs for various parts of the protein and solvent for the N $_\epsilon$ -H tautomer simulations. The differences in the average frequencies for B $_\epsilon$  and R $_\epsilon$  are almost entirely due to the electric field contribution of His64. The Stark effect frequency shift and the initial amplitudes of the FFCF for the solvent are essentially the same. The Stark frequency shifts are additive; the initial amplitudes of the FFCFs are not.

curve) in Figure 11. The parameters used in the calculations shown in Figures 10 and 11 are listed in Table 2. The agreement between the calculated and measured vibrational echo signals and linear spectra shown in Figures 10 and 11 is not very good when using the FFCFs derived from the  $N_{\delta}-H$  tautomer of His64. There are pronounced systematic differences in both the

fits to the dynamical line shapes and the calculation of the linear spectrum. In addition, the best fit value for the Stark coupling constant was found to be  $\lambda=1.4~{\rm cm^{-1}/(MV/cm)}$ , which lies well outside the experimental range for  $\lambda$  measured by Boxer and co-workers. <sup>64,65</sup> The calculated frequency splitting between the  $B_{\delta}$  and  $R_{\delta}$  state is 25 cm<sup>-1</sup>, a significant overestimate of the measured splitting 11 cm<sup>-1</sup>. A summary of the parameters used in the vibrational echo calculation for the  $N_{\delta}-H$  tautomer is given in Table 2.

Comparison of Figures 8 and 10 shows that the differences between the FFCFs for the two tautomers of His64 shown in Figure 6 give rise to very different spectrally resolved stimulated vibrational echo signals. The agreement between the measured vibrational echo data and the vibrational echo signals calculated using the  $N_{\rm e}-H$  tautomer of His64 is quite good, while the agreement with the measured vibrational echo data using the  $N_{\rm b}-H$  tautomer of His64 is significantly worse. Figure 11 shows that the predicted absorption spectrum for the  $N_{\rm b}-H$  tautomer also agrees poorly with the measured result. In addition, the value of the Stark coupling constant  $\lambda$  necessary to give reasonable agreement between the calculated vibrational echo data for the  $N_{\rm b}-H$  tautomer and the measured vibrational echo

![](_page_9_Figure_2.jpeg)

**Figure 9.** Comparison of the measured IR absorption spectrum of the CO stretch in MbCO (solid line) with that calculated using FFCFs for the  $N_\epsilon$ –H tautomer of His64 (dashed line). The measured spectrum shows three bands at  $\sim$ 1965, 1945, and 1934 cm<sup>-1</sup>. The calculated linear spectrum for the  $N_\epsilon$ –H tautomer is slightly wider than the measured spectrum, but generally agrees reasonably well with the overall shape of the experimental spectrum.

data is unphysically small. The best fit values of  $\lambda$  are 2.1 cm<sup>-1</sup>/ (MV/cm) for the  $N_{\epsilon}$ -H tautomer and 1.4 cm<sup>-1</sup>/(MV/cm) for the N<sub> $\delta$ </sub>-H tautomer of His64. A value of  $\lambda = 1.4$  cm<sup>-1</sup>/ (MV/cm) implies an extremely high (approaching infinitely high) dielectric constant for the heme pocket, inconsistent with what is known about the structure of the hydrophobic heme pocket. <sup>15,31,64,65,68</sup> The value of  $\lambda = 2.1$  cm<sup>-1</sup>/(MV/cm) obtained from fitting the vibrational echo data for the  $N_{\epsilon}$ -H tautomer lies within the range established by Park et al. using vibrational Stark effect spectroscopy.<sup>64,65,68</sup> It is possible to improve the quality of the agreement between the measured vibrational echo signals and those calculated using the  $N_{\delta}$ -H tautomer by increasing the  $A_1/A_3$  concentration ratio from 1.4 to around 4. However, a ratio of 4 is completely outside any error in the model independent fit to the linear spectrum used to determine the concentrations. In addition, using a ratio of 4 does not change the unphysical best fit value of  $\lambda = 1.4 \text{ cm}^{-1}/(\text{MV/cm})$  for the  $N_{\delta}$ -H tautomer.

Our finding that the vibrational echo data are best modeled by the dynamics of MbCO with the  $N_{\epsilon}$ -H structure is consistent with other measurements and calculations that have indicated that the N<sub>e</sub>-H tautomer is associated with the A<sub>1</sub> and A<sub>3</sub> substates. While two recent high-resolution X-ray crystal structures<sup>28,29</sup> disagree on the exact position and orientation of His64, both structures have  $N_{\epsilon}$  inside the pocket, close to the ligand. Given that this is the orientation of the His64 imidazole, if the tautomerization state of His64 were  $N_{\delta}$ -H, lone pair interactions between  $N_{\epsilon}$  and the CO ligand would blue-shift the CO transition frequency.<sup>20</sup> Rovira et al.<sup>20</sup> calculated the expected transition frequency of the CO stretching mode in MbCO for a number of different configurations and tautomerizations and concluded that only the  $N_{\epsilon}$ -H tautomer could reproduce the frequency shift trends seen experimentally. In addition, a recent electron nuclear double resonance (ENDOR) experiment<sup>69</sup> on MbNO assigned the tautomerization state of His64 to  $N_{\epsilon}$ -H. Our assignment of the tautomerization state of His64 to  $N_{\epsilon}$ -H

is consistent with the existing strong case for this tautomer state giving rise to the A<sub>1</sub> and A<sub>3</sub> substates of MbCO.

**C. Decomposition of the Contributions to Dephasing Using the MD Simulations.** Once the structural origins of the A substates of MbCO have been identified, the next step is to determine the source of the dynamical differences between these states. We can use the MD simulations to identify contributions to vibrational dephasing from different parts of the solvated MbCO system. The fluctuating Stark shift of the CO vibrational frequency in eq 1 is linear in the electric field at the CO, which may be decomposed into contributions from various parts of the system. The contribution to the frequency fluctuation from a collection of atoms denoted *j* is

$$\delta\omega_i(t) = \lambda[\vec{u}(t) \cdot \vec{E}_i(t) - \langle \vec{u} \cdot \vec{E}_i \rangle]$$
 (5)

where  $\vec{E}_j$  is the electric field at the midpoint of the CO bond, generated by the partial charges on the atoms in collection j. For example, we may decompose the total electric field at the CO into contributions from the protein and from the water solvent, so that the frequency fluctuation takes the form

$$\delta\omega(t) = \delta\omega_{\rm p}(t) + \delta\omega_{\rm s}(t) \tag{6}$$

with subscripts p and s labeling protein and solvent, respectively. The FFCF, C(t), is then decomposed into autocorrelation functions of frequency fluctuations induced by the protein and by the solvent and cross-correlations between frequency fluctuations from those sources:

$$\langle \delta \omega(t) \delta \omega(0) \rangle = \langle \delta \omega_{p}(t) \delta \omega_{p}(0) \rangle + \langle \delta \omega_{s}(t) \delta \omega_{s}(0) \rangle + \langle \delta \omega_{p}(t) \delta \omega_{s}(0) \rangle + \langle \delta \omega_{s}(t) \delta \omega_{p}(0) \rangle$$
(7)

This decomposition is illustrated for the A<sub>3</sub> state in Figure 12a, and for A<sub>1</sub> in Figure 12b, and listed in Table 3. In each panel, C(t) is shown in black,  $C_{pp}(t) = \langle \delta \omega_p(t) \delta \omega_p(0) \rangle$  is shown in red,  $C_{ss}(t) = \langle \delta \omega_s(t) \delta \omega_s(0) \rangle$  is shown in green, and the sum of the cross-correlation functions,  $C_{ps}(t) + C_{sp}(t) =$  $\langle \delta \omega_{\rm p}(t) \delta \omega_{\rm s}(0) \rangle + \langle \delta \omega_{\rm s}(t) \delta \omega_{\rm p}(0) \rangle$  is shown in blue. The black curve is thus the sum of the red, blue, and green curves. For the A<sub>3</sub> substate in Figure 12a,  $C_{pp}(t)$  is very similar to C(t), including the fine structure on the picosecond time scale. This similarity does not arise because the solvent contribution  $C_{\rm ss}(t)$ is negligible, but because of a near cancellation between  $C_{ss}(t)$ and the sum of solvent-protein cross-correlation functions,  $C_{\rm sp}(t) + C_{\rm ps}(t)$ . Each of these cross-correlation functions is negative, indicating that electric field fluctuations from protein and solvent are anticorrelated. The solvent contribution  $C_{ss}(t)$  lacks fine structure and is very similar for the two states. Figure 12b shows that  $C_{pp}(t)$  is also very similar to C(t) for the  $A_1$  substate, but that on the time scale of a few picoseconds, C(t) decays more slowly than  $C_{pp}(t)$ , because the cancellation between  $C_{\rm ss}(t)$  and  $C_{\rm sp}(t) + C_{\rm ps}(t)$  is not as complete as for the A<sub>3</sub> state.

We have further separated the protein contribution  $C_{\rm pp}(t)$  into contributions from the eight helices and connecting loops that compose Mb (see Figure 1). With the exception of helix E, which contains His64, the autocorrelation functions of induced frequency fluctuations for all the helices and loops are generally

<sup>(68)</sup> Park, E. S.; Andrews, S. S.; Hu, R. B.; Boxer, S. G. J. Phys. Chem. B 1999, 103, 9813-9817.

<sup>(69)</sup> Flores, M.; Wajnberg, E.; Bemski, G. Biophys. J. 2000, 78, 2107-2115.

<sup>70)</sup> In this decomposition, the subscript p includes the heme, but the FFCF for fluctuations in the CO vibrational frequency induced only by the heme is very similar for R<sub>ε</sub> and B<sub>ε</sub> and contributes little to the time dependence of the total FFCF in either state.

![](_page_10_Figure_1.jpeg)

**Figure 10.** Comparison of the measured vibrational echo data (black) with the calculated vibrational echo data (red) for the N*<sup>δ</sup>*-H tautomer of His64. Frequencies and values of *T*<sup>w</sup> are the same as those shown in Figure 8. The vibrational echo signals were calculated using the FFCFs shown in Figure 6b. The parameters used in the vibrational echo calculation are listed in Table 2. The agreement is poorer for the N*<sup>δ</sup>*-H tautomer of His64 than for the N-<sup>H</sup> tautomer of His64 shown in Figure 8.

small. However, we calculate systematic differences between the A3 state and the A1 state in the contributions of the B, C, and D helices to the FFCF. The dephasing contribution for all three of these helices is larger in the A1 state. The crosscorrelations between different helices are negligible, indicating that the helices move independently on these time scales. Dynamics of the residue Arg45 (see Figure 1) have been proposed to play a role in the transition between states A1 and A3. <sup>21</sup> We have computed the autocorrelation function of frequency fluctuations of the CO vibration from the electric field of Arg45 and find that these correlation functions are very similar for the two states, implying that the dynamics of this residue do not contribute to dephasing differences between A3 and A1.

We have carried out corresponding analysis to examine the contribution to *C*(*t*) from interactions between CO and the heme ring, including the Fe atom. While the heme ring contributes substantially to the average electric field at the CO, and hence to the total Stark shift of the CO frequency, heme dynamics71 do not contribute significantly to the electric field fluctuations at the CO on the time scales relevant to the vibrational echo. Moreover, contributions to *C*(*t*) from heme dynamics are nearly identical for the A1 and A3 substates. We have also ascertained that the mean bond length between Fe and the proximal histidine and the fluctuations in that bond length are identical in the A1 and A3 substates, as can be seen from Table 1. This finding suggests that, within the Stark effect model employed here, the proximal histidine is not a major contributor to dephasing differences between the two states. This classical mechanical model does not include polarization effects and other quantum mechanical phenomena that may play a role in the laboratory. However, as shown in Section IVB, the time-dependent Stark effect model is sufficient to describe the dephasing dynamics probed by the vibrational echo, and the magnitude of the Stark coupling constant is consistent with independent experimental measurements.64,65

The role of His64 in dephasing the CO vibration is investigated with the decomposition

$$\delta\omega(t) = \delta\omega_{\rm h}(t) + \delta\omega_{\rm r}(t)$$
 (8)

in which the first term denotes the contribution from His64 and (71) Sage, J. T.; Schomacker, K. T.; Champion, P. M. *J. Phys. Chem.* **<sup>1995</sup>**, *<sup>99</sup>*, 3394-3405.

![](_page_11_Figure_2.jpeg)

**Figure 11.** Comparison of the measured IR absorption spectrum (solid line) of the CO stretch in MbCO with that calculated using FFCFs for the <sup>N</sup>*<sup>δ</sup>*-H tautomer of His64 (dashed line). The linear spectrum for the N*<sup>δ</sup>*-<sup>H</sup> tautomer is calculated using the same line centers and concentrations used in the calculation of the linear spectrum for the N-H tautomer of His64 shown in Figure 9. The agreement between the measured and calculated linear spectrum for the N*<sup>δ</sup>*-H tautomer is quite poor.

the second term represents the contribution from the rest of the system, solvent and protein. This decomposition is shown in Figure 13a for A3 and in Figure 13b for A1, and listed in Table 3. In each panel, *C*(*t*) is shown in black, the His64 contribution, *C*hh(*t*), is shown in red, the contribution from the rest of the system, *C*rr(*t*), is shown in green, and the sum of the crosscorrelation functions, *<sup>C</sup>*rh(*t*) <sup>+</sup> *<sup>C</sup>*hr(*t*), is shown in blue. Figure 13a shows that for the A3 substate, *C*(*t*) is essentially identical to *C*hh(*t*) over the range of time scales investigated. *C*(*t*) follows *C*hh(*t*) in the initial rapid decay on the time scale of hundreds of femtoseconds, in the slower decay on the picosecond time scale, and in the ringing on the picosecond time scale. This plot shows that the autocorrelation function of frequency fluctuations induced by the rest of the system, solvent and protein, *C*rr(*t*), is not itself negligible, but is nearly canceled by the negative cross-correlation functions, *<sup>C</sup>*rh(*t*) <sup>+</sup> *<sup>C</sup>*hr(*t*). The ringing characterizing *C*(*t*) and *C*hh(*t*) for A3 is absent for A1, as shown in Figure 13b. For the A1 substate, *C*hh(*t*) decays on the time scale of hundreds of femtoseconds to an offset that is static on the time scale of the simulations. The initial decay of *C*(*t*) follows that of *C*hh(*t*) for A1. The slower decay of *C*(*t*) on the picosecond time scale follows the contribution from the rest of the system, *C*rr(*t*)*.*

These MD simulation results indicate that interactions with His64 play a central role in the dephasing dynamics of CO in MbCO. For the A3 state, interactions with His64 are the dominant dephasing contributor, and these interactions control CO dephasing on both the femtosecond and picosecond time scales. In the A1 state, His64 interactions control the initial rapid dephasing on the femtosecond time scale, but dephasing on slower time scales results from the combined effect of interactions with the rest of the protein and solvent. The differences in His64 contributions to the FFCF shown in Figure 13a and 13b might lead one to the conclusion that His64 dynamics are significantly different for the A1 and A3 substates, that is, that the imidazole ring undergoes larger amplitude motions in A3 than in A1. In fact, this is *not* the case. We have examined the motions of His64 in the A1 and A3 substates, and our analysis indicates that the dynamics of the imidazole ring of His64 are

![](_page_11_Figure_6.jpeg)

**Figure 12.** Decomposition of the FFCFs into contributions from the protein and from the solvent for the (a) A3 and (b) A1 states seen in MD simulations of MbCO. The total contribution (black), contribution from only the protein (red), contribution from only the solvent (green), and the cross-correlations between the protein and solvent (blue) are shown. For both the A1 and the A3 states, most of the dephasing is due to the protein. The protein and solvent dephasing contributions are anticorrelated.

very similar in the two substates. A quantitative calculation of the autocorrelation functions of the C*<sup>â</sup>*-C*<sup>γ</sup>* dihedral angle of His64 for the two states, not shown here, indicates that the dynamics of this angle are comparable for A1 and A3. In addition, the mean center-of-mass position of the imidazole ring is unchanged by transitions between states, and the meansquared fluctuations of this position are comparable for the two states. The essential difference for His64 between the A1 and A3 substates is the average dihedral angle. Of course, the magnitude and direction of the electric field of His64 felt at the CO ligand will be dramatically affected by the orientation of the imidazole ring. The different dephasing autocorrelation functions of His64 therefore appear to be reflections of structural differences between the A1 and A3 substates, rather than dynamical differences between these states. The larger value of *C*hh(0) for A3, as well as the presence of ringing on the picosecond time scale for A3, reflect these structural differences.

### **V. Concluding Remarks**

Multidimensional vibrational echo signals were measured for sperm whale MbCO, and the dephasing dynamics were found to be in agreement with dephasing dynamics calculated from

![](_page_12_Figure_1.jpeg)

**Figure 13.** Decomposition of the FFCFs into contributions from His64 and from the rest of the system for the (a)  $A_3$  and (b)  $A_1$  states observed in MD simulations of MbCO. The total contribution (black), contribution from only His64 (red), contributions from all other atoms (green), and the cross-correlations between the His64 and the rest of the system (blue) are all shown. His64 is the dominant dephasing source for the  $A_3$  state. The  $A_1$  state has a substantial portion of the short time dephasing contribution from His64, but the rest of the system contributes appreciably to the dephasing at longer times. The dephasing contribution for His64 is more strongly anticorrelated with its surroundings in the  $A_3$  state.

MD simulations for sperm whale MbCO with the  $N_\epsilon-H$  tautomer of His64. The two conformational substates  $B_\epsilon$  and  $R_\epsilon$  observed in the MD simulations were assigned to the  $A_1$  and  $A_3$  substates of MbCO. Dynamics of His64 constitute a major source of dephasing for the CO ligand, and orientational changes of this residue give rise to the  $A_1$  and  $A_3$  substates.

Our previous vibrational echo studies on MbCO<sup>40,45</sup> treated horse heart MbCO. We have also recently made detailed spectrally resolved stimulated vibrational echo measurements on horse heart MbCO and find the vibrational echo data to be essentially the same as those for sperm whale MbCO,<sup>72</sup> despite minor differences in the peak shapes and positions previously noted in the IR spectra. <sup>15,31</sup> Additionally, we are able to fit the horse heart vibrational echo data using the identical FFCFs derived from the MD simulations on sperm whale MbCO with very similar values of the Stark coupling constant  $\lambda$ , although with different values of the substate concentrations appropriate for horse heart MbCO. The primary structures of sperm whale

MbCO and horse heart MbCO differ at 20 residues.<sup>73</sup> The substitutions are generally conservative, and none of them is near the distal heme pocket. The ligand binding kinetics and heme affinity<sup>73</sup> (the dominant factor in determining folding stability<sup>74</sup>) for the two holoproteins are very similar. These facts strongly suggest that the structural assignments and dephasing dynamics for the A<sub>1</sub> and A<sub>3</sub> substates of sperm whale MbCO are also valid for horse heart MbCO, and also possibly for MbCO from other species.

Ultimately, the goal of understanding protein dynamics is to relate these dynamics to the biological function of the protein. The structural assignments of the A substates of MbCO and the identification of the sources of the vibrational dephasing of CO presented here represent a step toward that goal. Interpreting the stimulated vibrational echo experimental results with MD simulations has provided considerable insight into the structural and dynamical nature of the A substates of myoglobin. Further work toward identifying the functional consequences of these structural differences is needed. The combination of MD simulations and time-resolved spectroscopy can provide some of the atomic level details necessary to help understand the connection between protein structure and function.

**Acknowledgment.** We thank Ileana Stoica and Professor Ron Elber at Cornell University for helpful discussions regarding MOIL. K.A.M., I.J.F., A.G., B.L.M., and M.D.F. acknowledge the National Institutes of Health (1R01-GM61137) for support of this research. W.G.N., R.A., and R.F.L. acknowledge support from the National Science Foundation (CHE-0105623) and the Petroleum Research Fund of the American Chemical Society. The molecular dynamics portion of this research was carried out using the resources of the Cornell Theory Center, which receives funding from Cornell University, New York State, federal agencies, and corporate partners. K.A.M. was partially supported by an Abbott Laboratories Stanford Graduate Fellowship. W.G.N. acknowledges fellowship support from Cornell's IGERT program in nonlinear systems, funded by NSF Grant DGE-9870681. R.A. is a Research Fellow of the Japan Society for the Promotion of Science (2000).

# Appendix A - Calculation of the Vibrational Echo

We calculate the vibrational echo signal from third-order perturbation theory in the radiation—matter interaction. <sup>47,52</sup> The third-order nonlinear polarization can be expressed as the sum of eight relevant terms after application of the rotating wave approximation and the phase-matching condition  $k_s = k_2 + k_3$  $-\vec{k}_1$ . The material system is treated as a quantummechanical three-level system, coupled to a classical solvent that is treated within a second-order cumulant expansion. Within this approximation, the dynamics of the system can be described with a two-time autocorrelation function. Autocorrelation functions of fluctuations in the frequencies of one-quantum transitions are set equal to the classical mechanical autocorrelation function of frequency fluctuations in eq 2: C(t) =  $\langle \delta \omega_{10}(t) \delta \omega_{10}(0) \rangle = \langle \delta \omega_{21}(t) \delta \omega_{21}(0) \rangle$ . The autocorrelation function of fluctuations in a two-quantum frequency is given by  $\langle \delta \omega_{20}(t) \delta \omega_{20}(0) \rangle = 4 \langle \delta \omega_{10}(t) \delta \omega_{10}(0) \rangle$ , the lifetime of the second excited state is taken to be one-half that of the first excited

<sup>(73)</sup> Scott, E. E.; Paster, E. V.; Olson, J. S. J. Biol. Chem. 2000, 275, 27129–27136.

<sup>(74)</sup> Hargrove, M. S.; Olson, J. S. *Biochemistry* **1996**, *35*, 11310–11318.

state, 75 and the transition dipole moments are related by  $\mu_{21}$  =  $\sqrt{2}\mu_{10}$ , as appropriate for a nearly harmonic vibration.<sup>76</sup> Within this model, the eight response functions are given by 47,52

$$R_{1} = R_{2} = |\vec{\mu}_{10}|^{4} e^{-i\omega_{0}(t_{3}-t_{1})} e^{-(t_{1}+2t_{2}+t_{3})/2T_{1}} \exp(-g(t_{1}) + g(t_{2}) - g(t_{3}) - g(t_{2}+t_{1}) - g(t_{3}+t_{2}) + g(t_{1}+t_{2}+t_{3}))$$
(A1)

$$R_{3} = -|\vec{\mu}_{10}|^{2}|\vec{\mu}_{21}|^{2}e^{-i\omega_{0}(t_{3}-t_{1})}e^{i\Delta t_{3}}e^{-(t_{1}+2t_{2}+3t_{3})/2T_{1}}$$

$$\exp(-g(t_{1})+g(t_{2})-g(t_{3})-g(t_{2}+t_{1})-g(t_{3}+t_{2})+$$

$$g(t_{1}+t_{2}+t_{3})) \text{ (A2)}$$

$$R_4 = R_5 = |\vec{\mu}_{10}|^4 e^{-i\omega_0(t_1+t_3)} e^{-(t_1+2t_2+3t_3)/2T_1} \exp(-g(t_1) - g(t_2) - g(t_3) + g(t_2+t_1) + g(t_3+t_2) - g(t_1+t_2+t_3))$$
(A3)

$$R_{6} = - |\vec{\mu}_{10}|^{2} |\vec{\mu}_{21}|^{2} e^{-i\omega_{0}(t_{3}+t_{1})} e^{i\Delta t_{3}} e^{-(t_{1}+2t_{2}+3t_{3})/2T_{1}}$$

$$\exp(-g(t_{1}) - g(t_{2}) - g(t_{3}) + g(t_{2}+t_{1}) + g(t_{3}+t_{2}) - g(t_{1}+t_{2}+t_{3})) \text{ (A4)}$$

$$R_{7} = |\vec{\mu}_{10}|^{2} |\vec{\mu}_{21}|^{2} e^{-i\omega_{0}(t_{1}+2t_{1}+t_{3})} e^{i\Delta t_{2}} e^{-(t_{1}+2t_{2}+t_{3})/2T_{1}} \exp(g(t_{1}) - g(t_{2}) + g(t_{3}) - g(t_{2}+t_{1}) - g(t_{3}+t_{2}) - g(t_{1}+t_{2}+t_{3}))$$
(A5)

$$\begin{split} R_8 &= - |\vec{\mu}_{10}|^2 |\vec{\mu}_{21}|^2 e^{-i\omega_0(t_1 + 2t_2 + t_3)} e^{i\Delta(t_2 + t_3)} e^{-(t_1 + 2t_2 + 3t_3)/2T_1} \\ &\exp(g(t_1) - g(t_2) + g(t_3) - g(t_2 + t_1) - g(t_3 + t_2) - \\ &g(t_1 + t_2 + t_3)) \ \ (\text{A6}) \end{split}$$

where  $\omega_0$  is the fundamental transition frequency,  $\Delta$  is the anharmonicity, and  $T_1$  is the lifetime of the first vibrational excited state. Dynamics of the environment of the CO represented by the FFCFs enter these response functions through the line-broadening function, g(t):

$$g(t) = \int_0^t d\tau_1 \int_0^{\tau_1} d\tau_2 C(\tau_2)$$
 (A7)

The linear absorption spectrum of the CO vibration is calculated within the same approximations used to calculate the nonlinear polarization and is given as the Fourier transform of I(t), a weighted sum of contributions from the conformational substates:

$$I(t) = \sum_{\alpha} c_{\alpha} I_{\alpha}(t)$$
 (A8)

$$I_{\alpha}(t) = |\vec{\mu}_{10}|^2 e^{-i\omega_{\alpha}t} e^{-t/2T_1} e^{-g_{\alpha}(t)}$$
 (A9)

where the subscript  $\alpha$  is used to denote the different A substates of the protein.

## Appendix B - Fitting the Vibrational Echo for the **MbCO A Substates**

The  $A_1$  line center determined from Figure 7 is 1945 cm<sup>-1</sup>, and the anharmonicity is 25.3 cm<sup>-1</sup>, consistent with previous measurements for the anharmonicity of MbCO.<sup>77</sup> The lifetime of the  $A_1$  substate was measured to be  $T_1 = 16.5$  ps, and the  $A_3$ substate lifetime was measured to be  $T_1 = 14.7$  ps, as independently determined using pump-probe spectroscopy.<sup>40</sup>

The values for the center wavelengths for the A<sub>0</sub> and A<sub>3</sub> substates were determined by fitting the linear absorption spectrum of sperm whale MbCO to three Voigt line shapes, holding the center frequency for the A<sub>1</sub> substate fixed. The relative populations for the substates were assumed to be proportional to the relative areas under each Voigt line shape. Because of the strong overlap between the  $A_1$  and  $A_3$  substates, the relative concentrations derived from the fitting were not uniquely determined and showed some sensitivity to the initial parameters used in the fitting. Equally good fits to the linear spectrum could be obtained using relative ratios of A<sub>1</sub>/A<sub>3</sub> from 1.2 to 1.6. We chose to fix the ratio of  $A_1/A_3$  to 1.4, in reasonable agreement with a previously reported value for the  $A_1/A_3$  ratio of 1.25 using four Gaussian fitting functions.<sup>78</sup> The final values of the line centers and concentrations are in good agreement with previous measurements and assignments of these quantities.6,7,12,78

Because we have not identified the A<sub>0</sub> substate in the MD simulations, its dephasing dynamics must be approximated. Previous vibrational echo experiments on the MbCO mutant H64V over a wide range of temperatures have shown that this mutant has a dephasing rate that is approximately 20% slower than wild-type MbCO A<sub>1</sub> substate at all temperatures.<sup>79</sup> The linear spectrum for the H64V mutant is quite similar to the spectrum of the  $A_0$  substate in the wild-type protein. <sup>15,31,79</sup> It has also been suggested that the A<sub>0</sub> substate dephasing dynamics are slower than the dephasing dynamics of the A<sub>1</sub> substate.<sup>60</sup> We therefore chose to scale the amplitude of the FFCF used to model the A<sub>1</sub> state by 0.64 to give a FFCF for the A<sub>0</sub> substate. The factor 0.64 is the empirically determined scaling constant that gives a vibrational echo decay that is slower by  $\sim 20\%$ . The lifetime of this substate was assumed to be equal to the lifetime of the A<sub>1</sub> substate. While the dephasing function and lifetime for the A<sub>0</sub> substate are only approximate, the overall effect of the error in these approximations on the calculated vibrational echo data is small, because these substates represent  $\sim$ 5% of the total substate population and contribute even less to the vibrational echo signal.

The values for the A substate line centers and relative populations, along with the FFCFs derived from the MD simulations, were used as input parameters for the calculation of the spectrally resolved stimulated vibrational echo for both His64 tautomers. For the calculated vibrational echo signals in Figure 8, the FFCF for  $B_{\epsilon}$  (Figure 6a, blue curve) was used for  $A_1$ , the FFCF for  $R_{\epsilon}$  (Figure 6a, red curve) was used for  $A_3$ , and the FFCF for B<sub>e</sub> multiplied by 0.64 was used for A<sub>0</sub>. For the calculated vibrational echo signals in Figure 10, the FFCF for  $B_{\delta}$  (Figure 6b, blue curve) was used for  $A_1$ , the FFCF for

The total dephasing is overwhelmingly dominated by pure dephasing processes in this system and would be essentially unaffected by small errors in the second excited-state lifetime

<sup>(76)</sup> Fourkas, J. T.; Kawashima, H.; Nelson, K. A. J. Chem. Phys. 1995, 103, 4393-4407.

Rector, K. D.; Kwok, A. S.; Ferrante, C.; Tokmakoff, A.; Rella, C. W.; Fayer, M. D. *J. Chem. Phys.* **1997**, *106*, 10027–10036.
Potter, W. T.; Hazzard, J. H.; Choc, M. G.; Tucker, M. P.; Caughey, W. S. *Biochemistry* **1990**, *29*, 6283–6295.
Rector, K. D.; Rella, C. W.; Kwok, A. S.; Hill, J. R.; Sligar, S. G.; Chien, E. Y. P.; Dlott, D. D.; Fayer, M. D. *J. Phys. Chem. B* **1997**, *101*, 1468–1475.

<sup>(80)</sup> Unno, M.; Christian, J. F.; Olson, J. S.; Sage, J. T.; Champion, P. M. J. Am. Chem. Soc. 1998, 120, 2670–2671.

<sup>(81)</sup> Merchant, K. A.; Thompson, D. E.; Fayer, M. D. Phys. Rev. A 2002, 65, 023817.

R*<sup>δ</sup>* (Figure 6b, red curve) was used for A3, and the FFCF for B*<sup>δ</sup>* multiplied by 0.64 was used for A0. In each of the vibrational echo calculations, all three FFCFs used in the calculation were scaled by the square of the Stark effect parameter *λ* which was allowed to vary freely until the best possible agreement between the calculated and measured vibrational echo signals was obtained.

**Supporting Information Available:** Descriptions of the modifications to the MOIL force-field for the N-H tautomer of His64, and contour plots of multidimensional vibrational echo data at various *T*<sup>w</sup> values (PDF). This material is available free of charge via the Internet at http://pubs.acs.org.

JA035654X