"""
The problem
Find the sum of elements of a list
"""


def get_sum(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return  sum


nums = [56 , 43 , 67 , 89]

total = get_sum(nums)
print('The total of each elements : ' , total)

# Alternative solution

nums = [56 , 43 , 67 , 89]
total = sum(nums)

print('Sum of the numbers : ' , total)


