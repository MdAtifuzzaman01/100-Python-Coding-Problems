"""

The Problem
Convert a decimal number to binary number using a recursive function.
"""

## Recursive Function :
def dec_to_binary(n):
   if n > 1:
       dec_to_binary(n//2)
   print(n % 2,end = '')
## Decimal Number
num = int(input("Your decimal number: "))
dec_to_binary(num)
print(" ")