"""
The problem
For a given list, get the sum of each number in the list
"""

def get_sum(nums):
    sum = 0
    for sum in nums:
        sum = sum + num
    return sum


nums = [13, 89, 65, 42, 12, 11, 56]

total = get_sum(nums)
print("The total of each elements:", total)

# Alternative Solution

nums = [13, 11, 16, 78, 31, 128]

total = sum(nums)
print('largest number you entered is : ' , total)

