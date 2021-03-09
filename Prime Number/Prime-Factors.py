"""

The problem
Ask the user to enter a number. Then find all the primes factors for the number.
"""

def get_prime_factors(n):
    factors = []
    divisor = 2
    while n > 2:
        if (n % divisor == 0):
            factors.append(divisor)
            n = n / divisor
        else:
            divisor = divisor + 1
        return factors

num = int(input('Enter a number : '))
factors = get_prime_factors(num)
print(factors)