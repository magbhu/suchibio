# ------------------------------------------------------------------
# File name: reverse.py
#
# Reversing a DNA sequence is a common operation in genetics when dealing
# with a complementary strand. String slicing operation string[::-1]
# returns the desired result.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
# https://en.wikipedia.org/wiki/Primer_%28molecular_biology%29#/media/Fi
# http://www.ncbi.nlm.nih.gov/nuccore/226377833?report=fasta
# ------------------------------------------------------------------

zika_DNA = 'AATCCATGGTTTCT'
print('Zika segment\t\t:', zika_DNA)

reversed_zika_DNA = zika_DNA[::-1]
print('Reversed zika segment\t:', reversed_zika_DNA)
