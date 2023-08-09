# ------------------------------------------------------------------
# File name: motif_search.py
#
# re — Regular expression operations
# This module provides regular expression matching operations similar
# to those found in Perl.
#
# re.search(pattern, string, flags=0)
# Scan through string looking for the first location where the
# regular expression pattern produces a match, and return a
# corresponding match object. Return None if no position in the
# string matches the pattern.
#
# This program reports if a motif (ATG followed by zero or more any
# characters-non greedy-ending with TAA) is present in a DNA sequence,
# and prints the matched substring, the start and end indices.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/re.html#module-re
# https://docs.python.org/3/library/re.html#raw-string-notation
# https://docs.python.org/3/library/re.html#re.search
# https://docs.python.org/3/library/re.html#match-objects
# https://docs.python.org/3/library/re.html#re.compile
# http://www.ncbi.nlm.nih.gov/nuccore/XM_002295694.2?report=fasta
# ------------------------------------------------------------------

import re
import sys

DNA_sequence = 'AATGAAGGGCCGCTACGATAAGGAACTTCGTAATTTCAG'
print('DNA_sequence:', DNA_sequence)

motif = r'ATG.*?TAA'         # r for raw string
#motif = r'[ATG.*?TAA'       # This is an invalid regular expression
print('Motif:', motif)

# Checking if motif is a valid regular expression
try:
    re.compile(motif)
except:
    print('Invalid regular expression, exiting the program!')
    sys.exit()

match = re.search(motif, DNA_sequence)

if match:
    print('Found the motif   :', match.group())
    print('Starting at index :', match.start())
    print('Ending at index   :', match.end())
else:
    print('Did not find the motif.')
