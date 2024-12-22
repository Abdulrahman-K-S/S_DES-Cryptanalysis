"""First Round

This file contains the first round functionality giving the K1
"""

from utils import performPermutation, splitIntoHalves


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


def firstRoundFromBottom():
    """firstRoundFromBottom

    This function calculates the first round from the
    bottom and stops right before the XOR
    """
    pass


def calculateAllPossibleK1s():
    """calculateAllPossibleK1s

    This function takes the expanded right side from the plaintext
    and the possible 8-bits from the sBoxes and calculates all
    the possible first subkey K1
    """
    pass