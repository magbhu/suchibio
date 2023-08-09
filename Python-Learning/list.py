# -------------------------------------------------------------------
# File name: list.py
#
# Python compound data type list can be written as a list of
# comma-separated values (items) between square brackets [,,]. Lists might
# contain items of different types, but usually the items all have the
# same type. Unlike strings, lists are a mutable type, i.e. it is
# possible to change their content. Forward index starts with 0 and
# increases; backward index starts with -1 and decreases.
#
# The code below illustrates some of the basic list operations using the
# stop codons.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/introduction.html#lists
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# https://docs.python.org/3/library/stdtypes.html#lists
# https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
# https://en.wikipedia.org/wiki/DNA_codon_table
# ------------------------------------------------------------------

# Constructing a list
stop_codons = ['TAA', 'tAG']
print(stop_codons)

# Accessing an item in a list
first_stop_codon = stop_codons[0]
print(first_stop_codon)

# Modifying an item in a list
stop_codons[1] = 'TAG'
print(stop_codons)

# Appending an item to the end of a list
stop_codons.append('TGA')
print(stop_codons)

# Number of items in a list
number_of_stop_codons = len(stop_codons)
print('There are', number_of_stop_codons, 'stop codons')

# Convert list to a string
DNA_seq = ''.join(stop_codons)
print(DNA_seq)

# Convert string to a list
DNA_list = list(DNA_seq)
print(DNA_list)

# Slicing a list
second_codon = DNA_list[3:6]             # index 6 not included
print('Second codon:', second_codon)

# Copying a list
DNA_list_duplicate = DNA_list.copy()
print(DNA_list_duplicate)

# Insert, delete element
DNA_list_duplicate.insert(5, "?")
print(DNA_list_duplicate)
DNA_list_duplicate.pop(5)        # Can also use: del DNA_list_duplicate[5]
print(DNA_list_duplicate)
