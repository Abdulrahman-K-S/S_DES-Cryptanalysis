"""First Round

This file contains the first round functionality giving the K1
"""

from utils import performPermutation, splitIntoHalves , sBoxes , possible_input , XOR ,  extract_output


def firstRoundFromTop(plaintext):
    """firstRound
    
    This function calculates the first round from the
    top and stops right before the XOR

    Arguments:
        plaintext (str): The plaintext given.
    
    Return:
        (str, str, str): The left side L0, Expanded right side and the right side R0
    """
    permutated_data = performPermutation(plaintext, "initial")

    L0, R0 = splitIntoHalves(permutated_data)

    expanded_R0 = performPermutation(R0, "expansion")

    return L0, expanded_R0, R0


def firstRoundFromBottom(R1,L0):
    """firstRoundFromBottom

    This function calculates the first round from the
    bottom and stops right before the XOR

    Arguments:
        R1 (str): The right half of the ciphertext after the second round.
        L0 (str): The left half of the plaintext after the initial permutation.

    Returns:
        (list): A list of possible inputs to the S-boxes.
    """
    x=XOR(R1,L0,4)
    permutated_x=performPermutation(x, "p4-inverse")
    o1,o2=extract_output(permutated_x)
    i1,i2=sBoxes(o1,o2)
    final_inputs=possible_input(i1,i2)
    return final_inputs
    


def calculateAllPossibleK1s(final_inputs,expanded_R0):
    """calculateAllPossibleK1s

    This function takes the expanded right side from the plaintext
    and the possible 8-bits from the sBoxes and calculates all
    the possible first subkey K1

    Arguments:
        final_inputs (list): The possible 8-bit inputs derived from the S-boxes.
        expanded_R1 (str): The expanded right half of the plaintext.

    Returns:
        (list): A list of all possible K1 subkeys.
    """
    k1=[]
    for i in final_inputs:
        k1.append(XOR(expanded_R0,i,8))
    return k1