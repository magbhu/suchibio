# ------------------------------------------------------------------
# File name: while.py
#
# while EXPR:
#    statements
#
# while loop iterates the block of statements as long as EXPR remains True.
#
# To illustrate the usage of while statement, the code below first
# computes the number of appearances of a nucleotide base in a string 
# using Python's str.count() method. Then it computes the same number
# using a while statement, hoping to get the same answer.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://www.ncbi.nlm.nih.gov/nuccore/KC545393.1?report=fasta
# ------------------------------------------------------------------

DNA_seq = 'CGGACACACAAAAAGAATGAAGGATTTTGAATCTTTATTGTGTGCGAGTAACTACGAGGAAGATTAAAGA'
print('DNA sequence:', DNA_seq)

bp = 'T'
print('Base pair:', bp)

print('str.count():', DNA_seq.count(bp))

count = 0
index = 0

while index < len(DNA_seq):
    if bp == DNA_seq[index]:
        count += 1
    index += 1

print('Our while count:', count)
