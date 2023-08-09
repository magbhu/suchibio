# ------------------------------------------------------------------
# File name: motif_search_groups.py
#
# Match.group([group1, ...])
# Returns one or more subgroups of the match. If there is a single argument,
# the result is a single string; if there are multiple arguments, the result
# is a tuple with one item per argument. Without arguments, group1 defaults
# to zero (the whole match is returned). If a groupN argument is zero, the
# corresponding return value is the entire matching string; if it is in the
# inclusive range [1..99], it is the string matching the corresponding
# parenthesized (...) group.
#
# This program reports if a motif (ATG followed by zero or more any
# characters-non greedy-ending with TAA) is present in a DNA sequence
# and lists the groupings (two groups are the motif found and the characters
# between ATG and TAA in the found motif).
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/re.html#re.Match.group
# https://docs.python.org/3/library/re.html#module-re
# https://docs.python.org/3/library/re.html#raw-string-notation
# https://docs.python.org/3/library/re.html#re.search
# https://docs.python.org/3/library/re.html#match-objects
# http://www.ncbi.nlm.nih.gov/nuccore/XM_002295694.2?report=fasta
# ------------------------------------------------------------------

import re
import sys

DNA_sequence = 'AATGAAGGGCCGCTACGATAAGGAACTTCGTAATTTCAG'
print('DNA_sequence:', DNA_sequence)

motif = r'(ATG(.*?)TAA)'
print('Motif:', motif)

# Checking if motif is a valid regular expression
try:
    re.compile(motif)
except:
    print('Invalid regular expression, exiting the program!')
    sys.exit()

match = re.search(motif, DNA_sequence)

if match:
    print('group0           :', match.group(0))
    print('group0 start-end :', match.start(0), match.end(0))
    print('group1           :', match.group(1))
    print('group1 start-end :', match.start(1), match.end(1))
    print('group2           :', match.group(2))
    print('group2 start-end :', match.start(2), match.end(2))
    print('groups as tuples :', match.groups())
else:
    print('Did not find the motif.')
