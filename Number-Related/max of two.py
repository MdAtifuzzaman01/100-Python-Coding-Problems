"""
The problem
Find the max number of two numbers.
"""

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
if (num2 >= num1):
    largest = num2
else:
    largest = num1
print("Largest number you entered is: ", largest)

#Alternative Solution

num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second  Number: '))
largest = max(num1 , num2)
print('Largest number you entered is : ' , largest)

