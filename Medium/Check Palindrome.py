"""

The problem
Check whether a number is an Armstrong number.
"""

my_str = input('Enter a string : ')
rev_str = my_str[::-1]

if my_str == rev_str:
  print("It is palindrome")
else:
  print("It is not palindrome")
