"""permutation

This file contains the functions that will perform
the permutations on the bits of the plaintext & ciphertext
"""

import permutationMapping as pMapping


def performPermutation(data, type):
    """performPermutation

    This functions takes the type of permutations to
    perform and performs the permutation on the data given.

    Arguments:
        data (str): The data to perform the permutation on.
        type (str): The type of permutation to perform.
    
    Return:
        (str): The new data after the permutation.
    """
    mapping = None

    if type == "initial":
        mapping = pMapping.initial_permutation_map
    elif type == "inverse":
        mapping = pMapping.inverse_initial_permutation_map
    elif type == "p4":
        mapping = pMapping.permutation_4_map
    elif type == "p4-inverse":
        mapping = pMapping.permutation_4_inverse_map
    elif type == "expansion":
        mapping = pMapping.expansion_permutation_map
    elif type == "p10":
        mapping = pMapping.permutation_10_map
    elif type == "p8":
        mapping = pMapping.permutation_8_map

    try:
        return ''.join([data[i - 1] for i in mapping])
    except:
        print("Wrong permutation type!")
