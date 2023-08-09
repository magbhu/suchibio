# ------------------------------------------------------------------
# File name: find.py
#
# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found
# within the slice s[start:end]. Optional arguments start and end are 
# interpreted as in slice notation. Return -1 if sub is not found.
#
# str.rfind(sub[, start[, end]])
# Return the highest index in the string where substring sub is found,
# such that sub is contained within s[start:end]. Optional arguments 
# start and endare interpreted as in slice notation. Return -1 on failure.
# 
# str.index(sub[, start[, end]]) and str.rindex(sub[, start[, end]])
# are like find() and rfind() but raise ValueError when the substring 
# sub is not found.
#
# str.count(sub[, start[, end]])
# Return the number of non-overlapping occurrences of substring sub
# in the range [start, end]. Optional arguments start and end are
# interpreted as in slice notation.
#
# Code below compute the number and the locations of codon CAT in
# a DNA segment.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/stdtypes.html#str.find
# https://docs.python.org/3/library/stdtypes.html#str.rfind
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://en.wikipedia.org/wiki/D-loop
# http://www.ncbi.nlm.nih.gov/nuccore/AF176731.1?report=fasta
# ------------------------------------------------------------------

chimp = 'GTACCACCTAAGTACTGGCTCATTCATTACAACCGGTATGTACTTCGTACATTACTGCCAGTCACCATGA'
print('Chimp D-loop:', chimp)

codon = 'CAT'

# Check if subtring is in string
is_in = codon in chimp
print('Is codon', codon, 'in chimp:', is_in)

# .count() counts how many times sub appears in string
how_many = chimp.count(codon)
print('How many times', codon, 'appears in chimp:', how_many)

# .find() returns the lowest index
first_index = chimp.find(codon)
print('First', codon, 'index: ', first_index)

second_index = chimp.find(codon, first_index + len(codon))
print('Second',  codon, 'index: ', second_index)

# .find() returns -1 if cannot find sub in string
third_index = chimp.find(codon, 27, 55)
print('Third', codon, 'index: ', third_index)

# .rfind() returns the highest index
last_index = chimp.rfind(codon);
print('Last', codon, 'index: ', last_index)
