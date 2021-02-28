"""

Here the problem is to take two numbers from the users.
Calculate the result of second number power of the first number.
"""
# First solution:

base_numb = int(input("Give the base number : "))
power_numb = int(input("Give the power number : "))

result = base_numb ** power_numb

print("Your result is : ", result)

"""
We can solve it in one other way as well
"""
# Alternative solution:
base_numb = int(input("Give the base number : "))
power_numb = int(input("Give the power number : "))

result = pow(base_numb, power_numb)
print("Your result is:",  result)
