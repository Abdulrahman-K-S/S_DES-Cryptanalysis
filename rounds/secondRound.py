"""Second Round

This file contains the second round functionality giving the K2
"""

from utils import performPermutation, splitIntoHalves , Sboxes , possible_input , XOR ,  extract_output


def secondRoundFromTop(R1):
    """
    Calculate the second round from the top.

    This function performs the second round operation starting from the 
    top and stops right before the XOR operation.

    Arguments:
        R1 (str): The right half of the plaintext after the first round.

    Returns:
        str: The expanded version of R1.
    """
    expanded_R1 = performPermutation(R1, "expansion")

    return  expanded_R1


def secondRoundFromBottom(ciphertext,L1):
    """
    Calculate the second round from the bottom.

    This function computes the operations for the second round starting 
    from the bottom, stopping right before the XOR operation.

    Arguments:
        ciphertext (str): The ciphertext to be used.
        L1 (str): The left half of the plaintext after the first round.

    Returns:
        tuple: A tuple containing the possible inputs to the S-boxes
               and the right half of the ciphertext (R2).
    """
    initial_perm=performPermutation(ciphertext, "initial")
    L2, R2 = splitIntoHalves(initial_perm)
    y=XOR(L1,L2,4)
    permutated_y=performPermutation(y, "p4-inverse")
    o1,o2=extract_output(permutated_y)
    i1,i2=Sboxes(o1,o2)
    final_inputs=possible_input(i1,i2)
    return final_inputs ,R2
    


def calculateAllPossibleK2s(final_inputs,expanded_R1):
    """
    Calculate all possible K2 subkeys.

    This function takes the expanded right side from the plaintext and 
    the possible 8-bit inputs derived from the S-boxes to calculate all 
    the potential subkeys for the second round (K2).

    Arguments:
        final_inputs (list): The possible 8-bit inputs derived from the S-boxes.
        expanded_R1 (str): The expanded right half of the plaintext.

    Returns:
        list: A list of all possible K2 subkeys.
    """
    k2=[]
    for i in final_inputs:
        k2.append(XOR(expanded_R1,i,8))
    return k2