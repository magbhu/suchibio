# -------------------------------------------------------------------
# File name: read_from_file.py
#
# open(file, mode='r', buffering=-1, encoding=None, errors=None,
#       newline=None, closefd=True, opener=None)
# This function opens file and returns a corresponding file object.
# If the file cannot be opened, an OSError is raised. Once opened,
# you can write to file with myfile.write() or print('string', file = myfile)
# It is advantageous to use the with keyword when dealing with file
# objects because the file is properly closed after its suite finishes,
# even if an exception is raised at some point. If you are not using the 
# with keyword, then you should call myfile.close() to close the file.
#
# This program opens a file  and demonsrates several ways of reading it.
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
# ------------------------------------------------------------------

import sys

if len(sys.argv) == 1:
   print('Please provide a command line argument as a file name!')
   sys.exit()
else:
   myfile = sys.argv[1]

# Open the file for reading, and read the first five lines. Close file.
try:
    f = open(myfile, 'r')
except OSError as oserr:
    print('OS error:', oserr)
else:
    print(f.readline(), end = '')
    print(f.readline(), end = '')
    print(f.readline(), end = '')
    print(f.readline(), end = '')
    f.close()

print()

# Read all lines into a list
try:
    f = open(myfile, 'r')
except OSError as oserr:
    print('OS error:', oserr)
else:
    lines = f.readlines()
    number_of_lines = len(lines)
    print('There are', number_of_lines, 'lines in', myfile)
    f.close()

print()

# The best way to read all the lines of a file
try:
    with open(myfile, 'r') as f:
        for line in f:
            print(line, end='')
except OSError as oserr:
    print('OS error:', oserr)
