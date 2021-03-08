"""
The Problem
For a list, find the second smallest element in the list
"""

def get_second_smallest(nums):
    smallest =  nums[0]
    second_smallest = nums[0]
    for i in range(1 , len(nums)):
        if nums[i] < smallest:
            second_smallest = smallest
            largest = nums[i]
        elif nums[i] < second_smallest:
            second_smallest = nums[i]
    return  second_smallest

my_nums = [44, 78, 90 , 190 , 43]
second_smallest = get_second_smallest(my_nums)
print('Second smallest is : ' , second_smallest)

# Alternative solution

nums = [44, 78, 90 , 190 , 43]
nums.remove(min(nums))
second_smallest = min(nums)

print('Second smallest is : ', second_smallest)

