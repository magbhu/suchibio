# ------------------------------------------------------------------
# File name: if_else.py
#
# The compound statement if_else has the syntax
#
# if EXPR:
#    statements
# else:
#    statements
#
# If EXPR is True the first block of statements are executed, otherwise
# the second block of statements following else are executed.
#
# Code below determines if the first codon in a DNA segment
# is the start codon ATG or not and reports the result.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/controlflow.html?#if-statements
# https://docs.python.org/3/reference/compound_stmts.html?#the-if-statement
# https://docs.python.org/3/library/stdtypes.html?#truth-value-testing
# ------------------------------------------------------------------

DNA_segment = 'ATGACATGA'
codon1 = DNA_segment[0:3]

# == operator tests the equality of two strings, resulting in True/False
if (codon1 == 'ATG'):
    print('Codon', codon1, 'is a start codon.')
else:
    print('Codon', codon1, 'is not a start codon.')

print('Done!')
