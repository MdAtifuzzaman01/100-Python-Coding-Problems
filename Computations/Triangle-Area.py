import math

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of your triangle is ', area)