# ------------------------------------------------------------------
# File name: motif_search_interactive.py
#
# re.finditer(pattern, string, flags=0)
# Return an iterator yielding match objects over all non-overlapping
# matches for the re pattern in string. The string is scanned
# left-to-right, and matches are returned in the order found.
# Empty matches are included in the result.
#
# The program herein stores a DNA sequence in uppercase letters and 
# asks the user to enter a motif in regular expression. If the motif 
# is an invalid regular expression, it asks the user to enter another  
# motif. If the regular expression is valid, it finds all matches of 
# the motif in the DNA sequence and reports the matches, including 
# groups and positions. Matches are displayed in lowercase letters.
# If no motif is entered, the program terminates.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/re.html#re.finditer
# https://docs.python.org/3/library/re.html#module-re
# https://docs.python.org/3/library/re.html#raw-string-notation
# https://docs.python.org/3/library/re.html#re.compile
# http://www.ncbi.nlm.nih.gov/nuccore/XM_002295694.2?report=fasta
# ------------------------------------------------------------------
import re

DNA_sequence = 'AATGAAGGGCCGCTACGATAAGGAACTTCGTAATTTCAG'
print('DNA_sequence:', DNA_sequence)

while True:
    motif = input('Enter a motif to search for or enter to exit : ')
    if motif == '':
        break
    print('Motif:', motif)
    print('-'*len(DNA_sequence))
    # Checking if motif is a valid regular expression
    try:
        re.compile(motif)
    except:
        print('Invalid regular expression!')
    else:
       motif_found = False
       matches = re.finditer(motif, DNA_sequence)
       for match in matches:
           for i in range(0, len(match.groups()) + 1):
               print('group%02d %02d-%02d: %s' % (i, match.start(i), match.end(i), match.group(i)))
           DNA_sequence = DNA_sequence[0:match.start()] + match.group().lower() + DNA_sequence[match.end():]
           print('-'*len(DNA_sequence))
           motif_found = True
       if motif_found == True:
           print('Motif search is completed:')
           print(DNA_sequence)
           DNA_sequence = DNA_sequence.upper()
           print(DNA_sequence)
       else:
           print('Did not find any motif match!')
    print('~'*len(DNA_sequence))
print('Bye!')
