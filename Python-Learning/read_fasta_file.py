# -------------------------------------------------------------------
# File name: read_fasta_file.py
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
# Below, we will open a file containing information about a DNA sequence
# in FASTA format. Then we will read the file line-by-line, except
# line starting with > sign; remove newline characters and concatenate
# lines into a single string.
#
# The filename will be provided as a command line argument. This means
# that it will be supplied when we run our program, directly after
# the name of the program.  Example: read_fasta_file.py BRAC2.fasta
# Our program will exit if the file name is not provided,  or the file
# does not exist or cannot be opened.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/library/stdtypes.html#str.strip
# https://en.wikipedia.org/wiki/BRCA2
# http://www.ncbi.nlm.nih.gov/nuccore/XM_002295694.2?report=fasta
# ------------------------------------------------------------------

import sys

if len(sys.argv) == 1:
    print('Please provide a command line argument as a file name!')
    sys.exit()
else:
    myfile = sys.argv[1]

sequence = ''

try:
    with open(myfile, 'r') as f:
        for line in f:
            if '>' not in line:
                sequence = sequence + line.strip()
except OSError as oserr:
    print('OS error:', oserr)
else:
    print(sequence)
