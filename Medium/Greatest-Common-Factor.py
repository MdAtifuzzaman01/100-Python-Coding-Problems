"""
The Problem
Calculate the greatest common divisor (gcd) of two numbers.

"""

def compute_gcd(x, y):
	smaller = min(x,y)
	gcd = 1
	for i in range(1, smaller+1):
		if((x % i == 0) and (y % i == 0)):
			gcd = i
	return gcd

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = compute_gcd(num1, num2)

print("GCD of", num1,"and", num2,"is", gcd)

# Alternative solution
# Recursive GCD

def gcd (a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

a = int(input('Enter 1st number : '))
b = int(input('Enter 2nd number : '))

GCD = gcd(a,b)
print("GCD is :" ,  GCD)

# Another solution

#  Using Built GCD function
import math
a = int(input('Enter 1st Number : '))
b = int(input('Enter 2nd Number : '))

gcd = math.gcd(a , b)
print(gcd)