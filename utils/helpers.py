"""helpers

This file contains the helping functions like the swap, split
and combine
"""


def splitIntoHalves(data):
    """splitIntoHalves
    
    This function performs the splitting of input to 2 parts

    Arguments:
        data (str): The data to be split
    
    Return:
        (str, str): The left side L & The right side R
    """
    mid = len(data) // 2
    return data[:mid], data[mid:]
