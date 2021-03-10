"""

The problem
Reverse a string using a recursive function.
"""


def recursive_recur(str):
    if len(str) == 0:
        return str

    else:
        return recursive_recur(str[1:]) + str[0]

str = input('Enter your string : ')
rev_str = recursive_recur(str)
print('Reverse your string : ' , rev_str)