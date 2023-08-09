# ------------------------------------------------------------------
# File name: motif_findall.py
#
# re.findall(pattern, string, flags=0)
# Return all non-overlapping matches of pattern in string, as a list
# of strings. The string is scanned left-to-right, and matches are
# returned in the order found. If one or more groups are present in
# the pattern, return a list of groups; this will be a list of tuples
# if the pattern has more than one group. Empty matches are included
# in the result.
#
# This program finds all the occurrences of a motif
# in a DNA sequence and reports the motifs found as a list.
# The motif, in regular expression, here consists of
# substrings of A and/or T of lengths between 3 and 6, with two groups.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/re.html#re.findall
# https://docs.python.org/3/library/re.html#module-re
# https://docs.python.org/3/library/re.html#raw-string-notation
# https://docs.python.org/3/library/re.html#re.compile
# http://www.ncbi.nlm.nih.gov/nuccore/XM_002295694.2?report=fasta
# ------------------------------------------------------------------

import re
import sys

DNA_sequence = 'AATGAAGGGCCGCTACGATAAGGAACTTCGTAATTTCAG'
print('DNA_sequence:', DNA_sequence)

motif = r'(([AT]){3,6})'
print('Motif:', motif)

# Checking if motif is a valid regular expression
try:
    re.compile(motif)
except:
    print('Invalid regular expression, exiting the program!')
    sys.exit()

matches = re.findall(motif, DNA_sequence)

if matches:
    print('List of matches:', matches)
else:
    print('Did not find any match.')
