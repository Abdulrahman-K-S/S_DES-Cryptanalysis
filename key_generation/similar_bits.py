from utils import performPermutation, left_shift, splitIntoHalves

MASTER_KEY=[0,1,2,3,4,5,6,7,8,9]


def generate_keys(input_key):
    permuted_key = performPermutation(input_key, "p10")

    # Split the key into two halves
    left, right = splitIntoHalves(permuted_key)

    # Left Shift by 1 (LS-1)
    left = left_shift(left, 1)
    right = left_shift(right, 1)

    # Permutation P8 for K1
    K1 = performPermutation(left + right, 'p8')

    # Left Shift by 2 (LS-2)
    left = left_shift(left, 2)
    right = left_shift(right, 2)

    # Permutation P8 for K2
    K2 = performPermutation(left + right, 'p8')

    return K1, K2


def findPossiblePairs(possibleK1s, possibleK2s):
    """findPossiblePairs

    This function takes all the possible K1s & K2s and checks
    for the similairty in their bits to check for the pairs

    Arguments:
        possibleK1s (List): Contains all the possible K1s.
        possibleK2s (List): Contains all the possible K2s.

    Return:
        (List): All the possilbe pairs.
    """
    possible_pairs = []
    for k1_num, k1 in enumerate(possibleK1s):
        permutated_k1 = performPermutation(k1, "k1")
        for k2_num, k2 in enumerate(possibleK2s):
            permutated_k2 = performPermutation(k2, "k2")
            if permutated_k1 == permutated_k2:
                possible_pairs.append([f"K1 #{k1_num+1}: {k1}", f"K2 #{k2_num+1}: {k2}"])
                break
    return possible_pairs
