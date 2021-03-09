"""
The problem
Check whether a number is an Armstrong number.
"""

def check_armstrong(num):
    order = len(str(num))

    sum = 0

    # use temp to find each digit. Then power it
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order

        temp //= 10
    return  num == sum

num = int(input('Enter a number  : '))
if check_armstrong(num):
	print(num,"is an Armstrong number")
else:
	print(num,"is not an Armstrong number")