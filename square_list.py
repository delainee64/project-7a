# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 11/05/2022
# Description: Write a function named square_list that takes as a parameter
# a list of numbers and replaces each value with the square of that value.

def square_list(nums):
    """Replaces original value with the square of that value"""
    for ind in range(len(nums)):
        nums[ind] = nums[ind] * nums[ind]

# nums = [7, -3, 12, 9]
# square_list(nums)


# print(nums)
