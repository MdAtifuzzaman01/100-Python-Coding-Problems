# Here the problem is to find the floor division of two numbers.
import math
numb_1 = int(input("Enter a number : "))
numb_2 = int(input("Enter a number : "))

result = numb_1 // numb_2
print(result)

# We can do it in other way as well

# Alternative solution:
numb_1 = int(input("Enter a number : "))
numb_2 = int(input("Enter a number : "))

answer = math.floor(numb_1 / numb_2)

print("Your result is :", answer)

