---
layout: news-md
title: "How Scientists Encoded The Wizard of Oz Into DNA"
source_url: https://spectrum.ieee.org/dna-data-storage-method-sets-standard-for-highdensity-data-future
archived: 2026-08-28
---

**By Margo Anderson** · 27 Jul 2020 · *IEEE Spectrum*

*University of Texas researchers unveil protocol to shuffle large data stores into strands of genetic material*

---

Synthetic DNA as a high-density [data storage](https://spectrum.ieee.org/tag/data-storage) medium has [fascinated](https://spectrum.ieee.org/semiconductors/devices/exabytes-in-a-test-tube-the-case-for-dna-data-storage) [digital futurists](https://spectrum.ieee.org/the-human-os/biomedical/devices/dna-data-storage-gets-random-access) [for](https://spectrum.ieee.org/the-human-os/biomedical/devices/microsoft-sets-dna-datastorage-record) [years](https://spectrum.ieee.org/nanoclast/semiconductors/memory/dna-data-storage-just-got-a-bit-more-practical). The entire [internet](https://spectrum.ieee.org/tag/internet) could be coded into DNA strands that fit inside a shoebox, while the DNA molecule is so stable it can last tens of thousands or even hundreds of thousands of years. In 2013, for instance, scientists [sequenced the entire genome](https://doi.org/10.1038/nature12323) of a 700,000 year-old horse fossil.

The trick to date has involved shoehorning vast sums of bytes—a data standard tailor-made for linear and sequential stores like RAM and hard drives—into wet, squiggly forests of nano-sized deoxyribonucleic spaghetti noodles. Translating one data format to the other has been anything but straightforward.

Enter [William Press's team](https://www.oden.utexas.edu/people/348/) at the University of Texas at Austin. They've pioneered a set of DNA data encoding and decoding [algorithms](https://spectrum.ieee.org/tag/algorithms) that could jumpstart a new field of high-density, long-term data storage. Their work, reminiscent in its generative ambition of the landmark [BB84 protocol](https://en.wikipedia.org/wiki/BB84) that launched the field of [quantum cryptography](https://spectrum.ieee.org/tag/quantum-cryptography), could one day form the basis for a world of genomic data storage applications that come from reimagining information in terms of petabytes per gram.

Stephen Jones, a postdoc in Press's group and co-author of the *Proceedings of the National Academy of Sciences* [paper that describes their research](https://doi.org/10.1073/pnas.2004821117), says it's best to begin by understanding where data storage errors typically creep in. In traditional hard-drive and flash memory devices, bit-flips and erasures are the enemies of zeroes and ones.

"We have decades of beautiful work finding solutions to these two kinds of errors," Jones said. "But DNA is fundamentally different."

To make a workable [DNA data storage](https://spectrum.ieee.org/tag/dna-data-storage) standard, you need instead to worry about substitutions, insertions and deletions. The first is similar to a bit flip in which, say, an A nucleotide is substituted in the place where a T nucleotide used to be. (A, C, T and G and not 0 and 1 are the base language of DNA information.) The latter two classes of error represent cases, as the names suggest, where DNA base pairs are inserted or deleted from a strand.

Crucially, however, with DNA there is no reliable, inherent way of knowing that the strand you're reading off contains any substitution, insertion or deletion errors. There's no such thing as a countable and quantifiable DNA "memory register." Every base pair is just another nucleotide in a long sequence. And together they all form just another strand of DNA.

The relative nature of DNA data storage, in fact, is a key to Press, Jones and co-authors's HEDGES protocol (standing for Hash Encoded, Decoded by Greedy Exhaustive Search). No single isolated nucleotide in their protocol contains useable data. Rather, it's the accumulation of sequences of nucleotides that provides a robust storage system that they predict could achieve DNA's high-density potential while still enduring the eons.

The group used L. Frank Baum's *The Wizard of Oz*, translated into Esperanto no less, as their sample data set to be stored. Synthetic DNA these days, Jones said, typically comes in strands of one-hundred or so base pairs. That's the foundation of their "hard drive," as it were.

So their protocol needed to be able to be chopped up into thousands or millions of little hundred-nucleotide sequences that each contained the information required to reassemble the source text—even with an unknown number of substitution, insertion and deletion errors thrown in for good measure.

Encoding *The Wizard of Oz* into DNA, then, involved passing the data through an "outer" coding layer and an "inner" coding layer. (Think of these steps as two separate algorithms in a complex cryptographic standard.)

The outer layer diagonalized the source data so that any given strand of DNA would contain shards of many portions of the message. The inner layer, HEDGES, then translates each bit into an A, C, T or G according to an algorithm that depends both on the zero or one value of that bit plus additional information about its place in the data stream as well as the data bits immediately preceding it.

Then, once *Oz* is translated into the language of nucleotides, it's now ready to be written onto strands of synthetic DNA. Once encoded, the strands sat in storage where, Jones said, his job was to artificially age the genetic information—attempting to biochemically mutate the DNA strands and subjecting the sample to heat and cold damage.

"I beat the DNA up," he said. "Then after we'd beaten it up, we saw if we could recover *The Wizard of Oz*. The answer was Yes. It showed how robust DNA is. We had to really work hard to beat it up. It might be easier to do if you have 10,000 years buried in the earth or out in outer space or something. But we had to really accelerate the process."

Decoding the data from their DNA storage entailed first sequencing the *Wizard of Oz* genome and then translating that genetic data back into bits. Once they figure out which bits are "address" bits, they can string the remaining information bits back together into a single, concatenated data file.

Fellow postdoc and fellow co-author John Hawkins said one of the most attractive features of their new protocol is how robust it is to technological and data format changes over the centuries to come.

"Reading DNA will never become obsolete," he said. "Data surviving into the future is only half the problem. You still need to be able to read it on the other end. [But] DNA is uniquely future-proof on this front because we are made of it. As long as humans are made of DNA, we will always want machines around that can read it."

---

*Margo Anderson is senior associate editor and telecommunications editor at IEEE Spectrum. Illustration: iStockphoto.*

---

*Archived from [IEEE Spectrum](https://spectrum.ieee.org/dna-data-storage-method-sets-standard-for-highdensity-data-future) on 2026-08-28.*
