"""

The problem:
Take three sides of a triangle. And then calculate the area of the triangle.
"""


import math

a = float(input("Enter 1st Side : "))
b = float(input("Enter 2nd Side : "))
c = float(input("Enter 3rd Side : "))

# Calculate the semi-perimeter:

s =  (a + b+ c) / 2

# calculate the area
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of your triangle is : ', area)

