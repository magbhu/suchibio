# -------------------------------------------------------------------
# File name: strings.py
#
# String variable names in Python start with a letter followed by
# combination of letters, digits or underscore (no white spaces).
# String literals are enclosed in single '...' or double "..." quotes.
# Strings can be indexed, with the first character having index 0.
# Indices may also be negative, to start counting from the right  with -1.
# Python strings cannot be changed — they are immutable. Therefore,
# assigning to an indexed position in the string results in an error.
#
# The code below illustrates some of the basic string operations on a
# partial DNA and protein sequences of GFP.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/introduction.html#strings
# https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# https://docs.python.org/3/library/functions.html#len
# https://en.wikipedia.org/wiki/Green_fluorescent_protein
# https://www.nobelprize.org/prizes/chemistry/2008/summary/
# https://scienceblogs.com/pharyngula/2008/10/08/gfp-wins-nobel-prize
# https://en.wikipedia.org/wiki/DNA_codon_table
# ------------------------------------------------------------------

# String variables and literals
protein = "GFP"                    # Winner of 2008 Nobel in chemistry
protein_seq_begin = 'MSKGEELFTG'
protein_seq_end = 'HGMDELYK'

# Concatenation of strings
protein_seq = protein_seq_begin + '...' + protein_seq_end
print('Protein sequence of GFP: ' + protein_seq)

# String method str.upper()
DNA_seq = 'atgagtaaag...actatacaaa'
DNA_seq = DNA_seq.upper()
print('DNA sequence: ' + DNA_seq)

# Forward index starts with 0 and increases
# Backward index starts with -1 and decreases
print('The second nucleotide:', DNA_seq[1])
print('The last nucleotide:', DNA_seq[-1])

# Slicing a string
first_codon = DNA_seq[0:3]         # index 3 excluded
last_codon = DNA_seq[-3:]
print('First codon:', first_codon)
print('Last codon:', last_codon)
