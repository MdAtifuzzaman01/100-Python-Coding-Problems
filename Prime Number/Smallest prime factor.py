"""
The problem
Find the smallest prime factor for the given number.
"""


def get_smallest_factor(num):
    factor = 2
    while num % factor != 0:
        factor += 1
    return factor


num = int(input('Enter your number: '))

smallest_factor = get_smallest_factor(num)

print('The smallest prime factor is: ', smallest_factor)