"""permutation

This file contains the functions that will perform
the permutations on the bits of the plaintext & ciphertext
"""

from utils import permutationMapping


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
        mapping = permutationMapping.initial_permutation_map
    elif type == "inverse":
        mapping = permutationMapping.inverse_initial_permutation_map
    elif type == "p4":
        mapping = permutationMapping.permutation_4_map
    elif type == "p4-inverse":
        mapping = permutationMapping.permutation_4_inverse_map
    elif type == "expansion":
        mapping = permutationMapping.expansion_permutation_map
    elif type == "p10":
        mapping = permutationMapping.permutation_10_map
    elif type == "p8":
        mapping = permutationMapping.permutation_8_map
    elif type == "k1":
        mapping = permutationMapping.k1_map
    elif type == "k2":
        mapping = permutationMapping.k2_map

    try:
        return ''.join([str(data[i - 1]) for i in mapping])
    except:
        print("Wrong permutation type!")
