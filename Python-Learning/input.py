# ------------------------------------------------------------------
# File name: input.py
#
# input([prompt])
# If the prompt argument is present, it is written to standard output
# without a trailing newline. The function then reads a line from input,
# converts it to a string (stripping a trailing newline), and returns
# that. When EOF is read, EOFError is raised. input() returns a string;
# cast it if a number is expected.
#
# This program first prompts the user to type an NCBI sequence number
# and then echos it. Second, it illustrates the casting of string
# input with int() for use in arithmetical operations by calculating 
# the sum of two user-typed numbers.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/library/functions.html#input
# ------------------------------------------------------------------

sequence_number = input('Please type an NCBI sequence number: ')
print('Your sequence number is', sequence_number)

# Input returns a string
starting_index = input('Please type a starting index: ')
ending_index = input('Please type an ending index: ')
print('I will compute the number of bps in this region...')

# Must cast string inputs to int or float for arithmetical operations
number_of_bps = int(ending_index) - int(starting_index)
print('The number of bps is:', number_of_bps)
