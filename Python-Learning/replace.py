# ------------------------------------------------------------------
# File name: replace.py
#
# str.replace(old, new[, count])
# Return a copy of the string with all occurrences of substring old 
# replaced by new. If the optional argument count is given, only the 
# first count occurrences are replaced.
#
# The code below removes spaces and digits in a segment of DNA in 
# GenBank format and highlights the start codon ATG.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/stdtypes.html#str.replace
# http://www.ncbi.nlm.nih.gov/nuccore/226377833?report=genbank
# ------------------------------------------------------------------

import re

zika_DNA = '601 catgtgtgac gccaccatga gttatgagtg'
print('Original Zika DNA\t\t:', zika_DNA)

# Replace space with nothing one time
zika_DNA = zika_DNA.replace(' ', '', 1)
print('Replace space with nothing\t:', zika_DNA)

# Replace all space characters with nothing
zika_DNA = zika_DNA.replace(' ', '')
print('Replace spaces with nothing\t:', zika_DNA)

# Substitute all digits with nothing using regular expressions
zika_DNA = re.sub(r'[1234567890]', '', zika_DNA)
print('Replace numbers with nothing\t:', zika_DNA)
