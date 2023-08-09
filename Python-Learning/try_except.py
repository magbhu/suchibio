# ------------------------------------------------------------------
# File name: try_except.py
#
# Errors detected during execution are called exceptions. It is possible
# to write programs that handle selected exceptions with a try-except statement.
# The try statement works as follows:
# 1. The statement(s) between the try and except keywords is executed.
# 2. If no exception happens, the except block  is skipped and execution
#    of the try statement is finished.
# 3. If an exception occurs during execution of the try clause, the rest
#    of the clause is skipped. Then if its type matches the exception
#    named after the except keyword, the except clause is executed, and
#    then execution continues after the try statement.
# 4. An unhandled exception stops the execution.
# 5. Optional else clause must follow all except clauses. It is useful
#    for code that must be executed if the try clause does not raise
#    an exception.
#
# The code below illustrates the usage of try-except statement in handling
# exceptions, e.g. input error (ValueError), out-of-bound index error 
# (IndexError) in a list. The program asks for an input, repeatedly, if an 
# exception is raised. If no exception is raised, the program breaks out of the 
# infinite while loop by executing the else clause and finishes with 
# a message. One can also exit the program by typing Control^C.
# 
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/errors.html#exceptions
# https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
# https://docs.python.org/3/library/exceptions.html
# ------------------------------------------------------------------

import sys

stop_codons = ['TAA', 'TAG', 'TGA']
print('Stop codons:', stop_codons)

while True:
    try:
         index = int(input('Please enter the index of a stop codon to print: '))
         print('Your codon is', stop_codons[index])
    except ValueError as ve:
         print(ve, 'Try again...')
    except IndexError:
         print('Your index', index, 'is out of range. Try again...')
    except:
         print('Unexpected error:', sys.exc_info()[0])
         sys.exit()
    else:
         print('Good bye!')
         break
