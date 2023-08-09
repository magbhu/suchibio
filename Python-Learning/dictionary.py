# ------------------------------------------------------------------
# File name: dictionary.py
#
# A dictionary (dict) variable type is akin to a list that can hold
# a number of values. However, instead of indexing with integers, it
# uses a unique name, called a key, for each entry. A dict d = { }
# can be defined by comma-separated pairs of key and value, with
# a : in between, e.g. d = {"EcoRI" : "GAATTC"}.
#
# Code below illustrates some of the basic operations with a dictionary
# containing several restriction enzymes and their recognition sites.
#
# Version: 2.1
# Authors: H. Kocak and B. Koc
#          University of Miami and Stetson University
# References:
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# https://en.wikipedia.org/wiki/Restriction_enzyme
# ------------------------------------------------------------------

restriction_enzymes = {'EcoRI' : 'GAATTC',
                        'AluI' : 'AGCT',
                        'NotI' : 'GCGGCCGC',
                        'TaqI' : 'TCGA'
                      }

print(restriction_enzymes)
print()

# To get a list of keys from a dictionary view object
keys = list(restriction_enzymes.keys())
print('Keys as a list:', keys)

# To get a list of values from a dictionary view object
values = list(restriction_enzymes.values())
print('Values as a list:', values)

# To check if a key is in the dictionary
mykey = 'crispr'
check = mykey in restriction_enzymes
print('Is', mykey, 'key in the dictionary?', check)
print()

# To fetch a value from a dictionary with its key
EcoRI_value = restriction_enzymes['EcoRI']  #raises a KeyError if key not found
EcoRI_value = restriction_enzymes.get('EcoRI') # does not raise a KeyError if key not found
print('The recognition site of EcoRI is', EcoRI_value)
print()

# To add to an existing dictionary
restriction_enzymes['EcoRV'] = 'GATATC'
restriction_enzymes.update(EcoRV = 'GATATC')
print('With a new item:', restriction_enzymes)
print()

# To delete an item from a dictionary
del restriction_enzymes['EcoRV']
print('Original dictionary:', restriction_enzymes)
print()
