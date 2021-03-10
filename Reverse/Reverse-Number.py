"""
The problem
Reverse a number.
"""

def reverse_number(num):
    reverse = 0
    while (num > 0):
        last_digit = num % 10
        reverse = reverse*10 + last_digit
        num = num//10
    return reverse


n = int(input('Enter  a number : '))
reverse = reverse_number(n)
print('Reverse of the number : ' , reverse)