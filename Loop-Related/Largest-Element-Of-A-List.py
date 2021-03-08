"""

The problem:
Find the largest element of a list.
"""

# Solution


def get_largest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num
    return largest
my_nums = [67 , 87,98 ,0 ,65]

largest = get_largest(my_nums)

print('The largest number is : ', largest)

# Alternative Solution

nums = [67 , 87,98 ,0 ,65 , 10000]
largest = max(nums)
print('The largest number is ' , largest)

