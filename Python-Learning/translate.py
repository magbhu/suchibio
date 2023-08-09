# ------------------------------------------------------------------
# File name: translate.py
#
# static str.maketrans(x[, y[, z]])
# This static method returns a translation table usable for str.translate().
# If there are two arguments, they must be strings of equal length,
# and in the resulting dictionary, each character in x will be mapped
# to the character at the same position in y.
# If there is a third argument, it must be a string, whose characters
# will be mapped to None in the result.
#
# The code below computes the complementary strand of a DNA sequence.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/stdtypes.html#str.maketrans
# https://docs.python.org/3/library/stdtypes.html#str.translate
# http://www.ncbi.nlm.nih.gov/nuccore/226377833?report=fasta
# https://en.wikipedia.org/wiki/DNA
# ------------------------------------------------------------------

zika_DNA = 'AGTTGTTGATCTGTGTGAGTCAG'
print("Direct strand:        5' " + zika_DNA + " 3'")

complements = zika_DNA.maketrans('acgtACGT', 'tgcaTGCA')
complement_seq = zika_DNA.translate(complements)

bonds = " "*25 + "|"*len(zika_DNA)
print(bonds)
print("Complementary strand: 3' " + complement_seq + " 5'")
