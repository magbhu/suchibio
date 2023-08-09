# ------------------------------------------------------------------
# File name: concatenation.py
#
# Binary operator + concatenates two strings.
#
# The code below concatenates the first four codons for GFP.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://en.wikipedia.org/wiki/RNA_codon_table
# http://www.abcam.com/recombinant-a-victoria-gfp-protein-ab84191.html
# ------------------------------------------------------------------

GFP_seq = 'MSKGEELFTG...HGMDELYK'
print('Green fluorescent protein sequence:', GFP_seq)

M_codon = 'AUG'
S_codon = 'UCA'
K_codon = 'AAA'
G_codon = 'GGU'

RNA_seq = M_codon
RNA_seq = RNA_seq + S_codon
print('RNA sequence:', RNA_seq)

RNA_seq = RNA_seq + K_codon + G_codon
print(RNA_seq, 'could code amino acid sequence MSKG')
