"""permutationMapping

This file contains the mapping to all the permuations that
are present in the S-DES algorithm 
"""


initial_permutation_map = [
    2, 6, 3, 1, 4, 8, 5, 7
]

inverse_initial_permutation_map = [
    4, 1, 3, 5, 7, 2, 8, 6
]

permutation_4_map = [
    2, 4, 3, 1
]

permutation_4_inverse_map = [
    4, 1, 3, 2
]

expansion_permutation_map = [
    4, 1, 2, 3, 2, 3, 4, 1
]

permutation_10_map = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
permutation_8_map = [6, 3, 7, 4, 8, 5, 10, 9]

S0= [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
]

S1=[
        [0, 1, 2 ,3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
]