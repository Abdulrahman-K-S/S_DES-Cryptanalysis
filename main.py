from rounds import firstRoundFromTop, firstRoundFromBottom, calculateAllPossibleK1s, secondRoundFromBottom, secondRoundFromTop, calculateAllPossibleK2s
from key_generation import findPossiblePairs

if __name__ == "__main__":
    plaintext=input("Enter plaintext:") # 00010110
    ciphertext=input("Enter ciphertext:") # 10110111

    L0, expanded_R0, R0 = firstRoundFromTop(plaintext)

    round2_final_inputs, expanded_R1, R2 = secondRoundFromBottom(ciphertext, R0)

    round1_final_inputs = firstRoundFromBottom(R2, L0)

    possibleK1 = calculateAllPossibleK1s(round1_final_inputs, expanded_R0)
    possibleK2 = calculateAllPossibleK2s(round2_final_inputs, expanded_R1)

    possible_pairs = findPossiblePairs(possibleK1, possibleK2)
    if possible_pairs:
        for pair in possible_pairs:
            print(pair)
