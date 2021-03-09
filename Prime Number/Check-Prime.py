"""
The problem
For a given number, check whether the number is a prime number or not.
"""

def is_prime(num):
    for i in range(2 , num):
        if (num % 1) == 0:
            return  False
        return True


numb = int(input('Enter a number : '))

check_prime = is_prime(numb)

if check_prime:
    print('Your number is a prime number ')
else:
    print('Your number  is not a prime number ')

