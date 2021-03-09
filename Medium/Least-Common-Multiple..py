"""
The Problem
For two numbers, calculate the least common multiple (LCM).
"""


def calculate_lcm(x , y):
    lcm = max(x,y)
    while lcm % x != 0 or lcm % y != 0:
        lcm+=1
    return lcm

num1 = int(input('Enter 1st Number : '))
num2 = int(input('Enter 2nd Number : '))

lcm = calculate_lcm(num1,num2)

print(f"LCM of {num1} and {num2} is: {lcm}")