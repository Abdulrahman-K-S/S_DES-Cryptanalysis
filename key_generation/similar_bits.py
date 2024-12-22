from utils import performPermutation, left_shift

MASTER_KEY=[1,2,3,4,5,6,7,8,9,10]

def generate_keys(input_key):
    permuted_key = performPermutation(input_key,'p10')

    # Split the key into two halves
    left, right = permuted_key[:5], permuted_key[5:]

    # Left Shift by 1 (LS-1)
    left = left_shift(left, 1)
    right = left_shift(right, 1)

    # Permutation P8 for K1
    K1 = performPermutation(left + right, 'p8')

    # Left Shift by 2 (LS-2)
    left = left_shift(left, 2)
    right = left_shift(right, 2)

    # Permutation P8 for K2
    K2 =performPermutation(left + right, 'p8')

    return str(K1),str(K2)

def similar_bits(k1,k2):
    s_bits=[]
    for i in range(8):
        if k1[i]==k2[i]:
            s_bits.append(i)
    return s_bits


h1,h2=generate_keys(MASTER_KEY)
similar_bit=similar_bits(h1,h2)
print(similar_bit)