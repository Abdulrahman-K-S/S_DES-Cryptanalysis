"""helpers

This file contains the helping functions like the swap, split
and combine
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
    ctr=0
    size=len(s0)*len(s1)
    inputs=[-1]*size
    for i in s0:
        for j in s1:
            inputs[ctr]=i + j
            ctr+=1
    return inputs

def XOR(ep,input,b):
    temp=int(ep,2) ^ int(input,2)
    return f"{temp:0{b}b}"

def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def extract_output(output):
    output1=''
    output2=''
    output1 = f"{output[0]}{output[1]}"  
    output2 = f"{output[2]}{output[3]}"  
    output1 = int(output1, 2)
    output2 = int(output2, 2)
    return output1,output2

