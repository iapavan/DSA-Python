"""Problem Statement
Given an integer array nums, move all 0s to the end of the array 
while maintaining the relative order of all non-zero elements.
You must modify the array in-place.
Do not create another array to store the result.
nums = nums = [1, 0, 2, 0, 4]
output : [1, 2, 4, 0, 0]
"""
def remove_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            if fast != slow:
                nums[slow] = nums[fast]
            slow += 1
    diff = len(nums) - slow
    for i in range(diff):
        nums[slow] = 0
        slow += 1
    return nums
print(remove_zeroes(nums = [1, 0, 2, 0, 4]))