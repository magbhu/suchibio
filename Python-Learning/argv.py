# ------------------------------------------------------------------
# File name: argv.py
#
# Command line arguments are provided directly after the name of the
# program and they are stored as a list in sys.argv. The first entry
# sys.argv[0] is the script name (it is operating system dependent
# whether this is a full pathname or not).
#
# Our program will print out the list of arguments; will exit if
# no argument is provided. Example usage: args.py zika_DNA.fasta
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/interpreter.html#argument-passing
# https://docs.python.org/3/library/sys.html
# https://docs.python.org/3/using/cmdline.html#command-line-and-environment
# ------------------------------------------------------------------

import sys

if len(sys.argv) == 1:
   print('Please provide a command line argument!')
   sys.exit()

print('sys.argv list:', sys.argv)
print('The first argument:', sys.argv[0])
print('The second argument:', sys.argv[1])
