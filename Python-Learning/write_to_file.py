# -----------------------------------------------------------------
# File name: write_to_file.py
#
# open(file, mode='r', buffering=-1, encoding=None, errors=None,
#       newline=None, closefd=True, opener=None)
# This function opens file and returns a corresponding file object.
# If the file cannot be opened, an OSError is raised. Once opened,
# you can write to file with myfile.write() or print('string', file = myfile)
# It is advantageous to use the with keyword when dealing with file
# objects because the file is properly closed after its suite finishes,
# even if an exception is raised at some point.
#
# Code below opens a file and writes information about a DNA sequence
# in FASTA format. At the end, it reports if the file is created.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# http://www.esa.int/Our_Activities/Space_Science/Rosetta/Science_on_the_surface_of_a_comet
# https://en.wikipedia.org/wiki/DNA_codon_table
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/library/functions.html#print
# ----------------------------------------------------------------

import os.path

filename = 'Rosetta_partial.fasta'

with open(filename, 'w') as f:
    print('>JB_007 Rosetta partial genome', file=f)
    f.write('ATG')
    f.write('GGT')
    f.write('GGC')
    f.write('GGA')
    f.write('GGG')
    f.write('TGA')
    f.write('xxxACCATG')
    f.write('\n')

if os.path.isfile(filename):
   print('Rosetta partial genome is written to', filename, 'file successfully!')
