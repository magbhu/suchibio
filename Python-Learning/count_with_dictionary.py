# ------------------------------------------------------------------
# File name: count_with_dictionary.py
#
# Code below counts the number of each codon that appears in a DNA
# segment using a dictionary. Keys are the present codons and the values
# are their numbers.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/stdtypes.html#list
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# http://www.ncbi.nlm.nih.gov/nuccore/XM_002295694.2?report=fasta
# http://www.opensourceshakespeare.org/stats/
# ------------------------------------------------------------------

DNA_seq = 'gggtgcgacgattcattgttttcggacaagtggataggcaaccactaccggtggattgtc'
print('Sequence:', DNA_seq)

# Count the number of codons
DNA_length = len(DNA_seq)
number_of_codons = int(DNA_length/3)
print()

# Put codons in a list
codon_list = []
for i in range(number_of_codons):
    codon_list.append(DNA_seq[i*3:i*3 + 3])

print('List of codons:', codon_list)
print()

#Create codon counter dictionary (codon : codon_count)
codon_counter = {}

for codon in codon_list:
    if codon not in codon_counter:
        codon_counter[codon] = 1
    else:
        codon_counter[codon] += 1

# This loop syntax accesses the whole dictionary by looping
# over the .items() tuple list, accessing one (key, value)
# pair at each step.
print('Codon counter:')
for key, value in codon_counter.items():
    print(key, ':', value)
