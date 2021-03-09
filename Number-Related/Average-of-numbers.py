"""

The problem
Take numbers from a user and show the average of the numbers the user entered.
"""

len = int(input('How many numbers you want to enter ? : '))
nums = []

for i in range(0 , len):
    element = int(input('Enter element: '))
    nums.append(element)

total = sum(nums)
avg = total/len
print("Average of elements you entered",round(avg,2))

# Alternative solution

len = int(input("How many numbers you want to enter: "))

total = 0

for i in range(0, len):
    elem = int(input("Enter element: "))
    total += elem

avg = total / len
print("Average of elements you entered", round(avg, 2))