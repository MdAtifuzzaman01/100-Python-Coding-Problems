"""
The Problem
Converta decimal number to a binary number
"""

#Solution
def dec_to_binary(n):
    bits = []

    while n > 0:
        bits.append(n % 2)
        n = n // 2
    bits.reverse()

    binary = ''
    for bit in bits:
        binary += str(bit)
    return binary


num = int(input("Your decimal number: "))
binary = dec_to_binary(num)
print("Your binary is:", binary)