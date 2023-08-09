# ------------------------------------------------------------------
# File name: motif_finditer.py
#
# re.finditer(pattern, string, flags=0)
# Return an iterator yielding match objects over all non-overlapping
# matches for the re pattern in string. The string is scanned
# left-to-right, and matches are returned in the order found.
# Empty matches are included in the result.
#
# The program herein finds all the occurrences of a motif
# in a DNA sequence and reports the motifs found as a match object
# which contains position information.
# The motif, in regular expression, here consists of
# substrings of A and/or T of lengths between 3 and 6, with one group.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/re.html#re.finditer
# https://docs.python.org/3/library/re.html#finding-all-adverbs
# https://docs.python.org/3/library/functions.html#any
# https://docs.python.org/3/library/re.html#module-re
# https://docs.python.org/3/library/re.html#raw-string-notation
# https://docs.python.org/3/library/re.html#re.compile
# http://www.ncbi.nlm.nih.gov/nuccore/XM_002295694.2?report=fasta
# ------------------------------------------------------------------

import re
import sys

DNA_sequence = 'AATGAAGGGCCGCTACGATAAGGAACTTCGTAATTTCAG'
print('DNA_sequence:', DNA_sequence)

motif = r'([AT]){3,6}'
print('Motif:', motif)

# Checking if motif is a valid regular expression
try:
    re.compile(motif)
except:
    print('Invalid regular expression, exiting the program!')
    sys.exit()

motif_found = False
matches = re.finditer(motif, DNA_sequence)

for match in matches:
    print('-'*20)
    print('%02d-%02d: %s' % (match.start(0), match.end(0), match.group(0)))
    print('%02d-%02d: %s' % (match.start(1), match.end(1), match.group(1)))
    motif_found = True

if motif_found == False:
    print('Did not find any motif match!')
