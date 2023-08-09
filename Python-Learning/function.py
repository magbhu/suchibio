# ------------------------------------------------------------------
# File name: function.py
#
# The keyword def introduces a function definition. It must be followed
# by the function name and the parenthesized list of formal parameters.
# The statements that form the body of the function start at the next line,
# and must be indented. Variables in a function are local to that function.
#
# The first statement of the function body can optionally be a string literal
# enclosed in triple quotes ''' ... '''; this string literal is the 
# function’s documentation string, or docstring. 
#
# The user-defined function below takes a DNA segment as a string
# and returns the corresponding RNA segment as a string.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# https://docs.python.org/3/reference/compound_stmts.html#function-definitions
# https://docs.python.org/3/tutorial/controlflow.html#documentation-strings
# http://www.ncbi.nlm.nih.gov/nuccore/226377833?report=fasta
# ------------------------------------------------------------------

def DNAtoRNA(dna):
    '''
    Converts DNA string to RNA string.

    Parameters: DNA sequence as a string
    Return: RNA sequence as a string
    '''
    transliterate = dna.maketrans('tT', 'uU')
    rna = dna.translate(transliterate)
    return rna

# Can access the doctring ''' ... ''' with print(DNAtoRNA.__doc__)

zika_DNA = 'AGTTGTTGATCTGTGTGAGTCAGACTGCG'
print('Zika DNA segment is', zika_DNA)

zika_RNA = DNAtoRNA(zika_DNA);
print('Zika RNA segment is', zika_RNA)
