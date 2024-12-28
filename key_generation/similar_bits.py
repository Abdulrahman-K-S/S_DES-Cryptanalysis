from utils import performPermutation, left_shift, splitIntoHalves, concatenate

MASTER_KEY = "0123456789"


def generate_subkeys(master_key):
    """generate_subkeys
    
    This function takes in a Master Key and generates the
    2 sub-keys needed for performing the S-DES encryption/decryption

    Arguments:
        master_key (str): The master key

    Return:
        (str, str): Both subkeys K1 & K2
    """
    permuted_key = performPermutation(master_key, "p10")

    left, right = splitIntoHalves(permuted_key)

    left = left_shift(left, 1)
    right = left_shift(right, 1)

    K1 = performPermutation(concatenate(left, right), 'p8')

    left = left_shift(left, 2)
    right = left_shift(right, 2)

    K2 = performPermutation(concatenate(left, right), 'p8')

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
