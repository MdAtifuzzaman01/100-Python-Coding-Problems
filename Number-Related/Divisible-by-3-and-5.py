"""
The problem
For a given number, find all the numbers smaller than the number.
Numbers should be divisible by 3 and also by 5.
"""

def divisible_by_3_and_5(num):
    result = [ ]
    for i in range(num):
        if i%3 == 0 and i%5 == 0:
            result.append(i)
        return result

num = int(input('Enter   a number: '))
result = divisible_by_3_and_5(num)
print(result)