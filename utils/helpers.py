"""helpers

This file contains the helping functions like the swap, split
and combine as well as S-box processing and other utility functions.
"""
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

def Sboxes(output1,output2):
    """
    Identify possible inputs to S-boxes based on given outputs.

    Arguments:
        output1 (int): The output value for S-box S0.
        output2 (int): The output value for S-box S1.

    Returns:
        tuple: Two lists containing possible inputs for S-box S0 and S1.
    """
    possible_inputs1=[]
    possible_inputs2=[]
    for i in range(4):
        for j in range(4):
            if S0[i][j] == output1:
                row = f"{i:02b}"
                col = f"{j:02b}" 
                formatted_input = f"{row[0]}{col}{row[1]}"
                possible_inputs1.append(formatted_input)
            if S1[i][j] == output2:
                row=f"{i:02b}"
                col=f'{j:02b}'
                formatted_input = f"{row[0]}{col}{row[1]}"
                possible_inputs2.append(formatted_input)
    return possible_inputs1,possible_inputs2

def possible_input(s0,s1):
    """
    Combine all possible S-box inputs.

    Arguments:
        s0 (list): Possible inputs for S-box S0.
        s1 (list): Possible inputs for S-box S1.

    Returns:
        list: A list of concatenated inputs from S0 and S1.
    """
    ctr=0
    size=len(s0)*len(s1)
    inputs=[-1]*size
    for i in s0:
        for j in s1:
            inputs[ctr]=i + j
            ctr+=1
    return inputs

def XOR(ep,input,b):
    """
    Perform XOR operation between two binary strings.

    Arguments:
        ep (str): The first binary string.
        input (str): The second binary string.
        b (int): The bit-length of the result.

    Returns:
        str: The result of the XOR operation as a binary string.
    """
    temp=int(ep,2) ^ int(input,2)
    return f"{temp:0{b}b}"

def left_shift(bits, shifts):
    """
    Perform a left circular shift on the given bits.

    Arguments:
        bits (str): The binary string to shift.
        shifts (int): The number of positions to shift.

    Returns:
        str: The shifted binary string.
    """
    return bits[shifts:] + bits[:shifts]

def extract_output(output):
    """
    Extract two parts from a 4-bit output.

    Arguments:
        output (str): A 4-bit binary string.

    Returns:
        tuple: Two integers representing the extracted parts.
    """
    output1=''
    output2=''
    output1 = f"{output[0]}{output[1]}"  
    output2 = f"{output[2]}{output[3]}"  
    output1 = int(output1, 2)
    output2 = int(output2, 2)
    return output1,output2

