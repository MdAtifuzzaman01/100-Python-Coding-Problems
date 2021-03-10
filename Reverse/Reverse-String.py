"""

The problem
Reverse a string.
"""

def reverse_string(str):
    reverse = ''
    for char in str:
        reverse = char + str
    return reverse

str = input('Enter your string : ')
result = reverse_string(str)
print(result)