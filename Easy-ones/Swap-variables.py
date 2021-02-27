"""
Swap two variables.

To swap two variables:
The value of the first variable will become the value of the second variable.
On the other hand, the value of the second variable will become the value of the first variable.
"""
# Solution :
x = 7
y = 10
print( "x , y : ", x, ',', y)
# swap these two
temp = x
x = y
y = temp
print('x,y :', x,  ',', y)

# Alternative solution:
a = 5
b = 8
print( 'a , b : ', a, ",", b)
# swap these two
a,b = b,a
print("a ,b :",  a, ",", b)

# Another solution / trick if both the variables   are  number:

m = 8
v = 17
print( "m , v : ", m, "," , v)
m = m + v
v = m - v
m = m - v

print(" m ,v :", "," , m, "," , v)





