# ------------------------------------------------------------------
# File name: length.py
#
# Built-in function len(s)
# Return the length (the number of items) of an object. The argument
# may be a sequence (such as a string, bytes, tuple, list, or range)
# or a collection (such as a dictionary, set, or frozen set).
#
# Code below computes the number of nucleotides in a DNA segment.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/functions.html#len
# http://www.ncbi.nlm.nih.gov/nuccore/226377833?report=fasta
# ------------------------------------------------------------------

zika_DNA = 'AGTTGTTGATCTGTGT'
zika_DNA_length = len(zika_DNA)

print('The first', zika_DNA_length, 'nucleotides',
      'of Zika virus DNA are', zika_DNA)
