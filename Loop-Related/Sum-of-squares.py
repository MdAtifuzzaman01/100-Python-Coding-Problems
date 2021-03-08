"""
The Problem:
Find the sum of squares
"""


def square_sum(num):
    sum = 0
    for i in range(num + 1):
        square = ( i ** 2)
        sum = sum+ square

    return  sum

num = int(input('Enter a number : '))
sum = square_sum(num)

print('Sum of square is : ' , sum)

# Alternative Solution

def sum_of_square2(n):
    sum = n*(n+1)*(2*n+1)/6
    return sum

num = int(input('Enter a number: '))
sum = sum_of_square2(num)
print('Your sum of Square is: ', sum)