"""
The Problem
For a list, find the second largest number in the list.
"""

def get_second_largest(nums):
    largest =  nums[0]
    second_largest = nums[0]
    for i in range(1 , len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest:
            second_largest = nums[i]
    return  second_largest

my_nums = [44, 78, 90 , 190 , 43]
second_largest = get_second_largest(my_nums)
print('Second largest is : ' , second_largest)

"""
Alternative / Clever Solution:
"""

nums = [44, 78, 90 , 190 , 43]
nums.remove(max(nums))
second_largest = max(nums)
print('Second largest is : ' , second_largest)
