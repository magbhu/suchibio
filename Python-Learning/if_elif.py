# ------------------------------------------------------------------
# File name: if_elif.py
#
# The compound statement if_elif_else has the syntax
#
# if EXPR1:
#    statements1
# elif EXP2:
#     statements2
# else:
#    statements3
#
# If EXPR1 is True, the first group of statements1 are executed and
# the rest is skipped; otherwise, if EXPR2 is True, the statements2
# are executed; otherwise, statements3 are executed.
# There can be zero or more elif parts, and the else part is optional.
# The keyword ‘elif’ is short for ‘else if’, and is useful to avoid
# excessive indentation.
# An if … elif … elif … sequence is a substitute for the switch or
# case statements found in other languages.
#
# Code below determines if the last codon in a DNA segment
# is the start codon ATG or one of the stop codons TAA, TAG, or TGA;
# or none of the above.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/controlflow.html?#if-statements
# https://docs.python.org/3/reference/compound_stmts.html?#the-if-statement
# https://docs.python.org/3/library/stdtypes.html?#truth-value-testing
# https://docs.python.org/3/tutorial/datastructures.html?#comparing-sequences-and-other-types
# https://en.wikipedia.org/wiki/DNA_codon_table
# ------------------------------------------------------------------

DNA_segment = 'ATGACATGACCAATC'
codon1 = DNA_segment[-3:]

# == operator tests the equality of two strings, resulting in True/False
if (codon1 == 'ATG'):
    print('Codon', codon1, 'is a start codon.')
elif ((codon1 == 'TAA') or
     (codon1 == 'TAG') or
     (codon1 == 'TGA')):
    print('Codon', codon1, 'is a stop codon.')
else:
    print('Codon', codon1, 'is neither a start nor a stop codon.')

print('Done!')
