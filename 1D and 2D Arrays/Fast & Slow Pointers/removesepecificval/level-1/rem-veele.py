"""
Problem 2: Remove All Negative Numbers
Given an integer array, move all non-negative numbers to the beginning 
while maintaining their relative order.

Input:
nums = [-1, 3, -2, 5, 0, -4, 7]
Expected Output:
[3, 5, 0, 7, ...]

Return the number of valid elements.
Challenge: Don't write an element if it is already in its correct position.
"""
def remove_negative_element(nums):
    fast = 0
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] >= 0:
            if fast != slow:
               nums[slow]=nums[fast]
            slow += 1
    return slow
    """
    diff = len(nums)-slow
        for i in range(diff):
            nums[slow] = 0
            slow += 1
        return nums
    """  
    
    
print(remove_negative_element([-1, 3, -2, 5, 0, -4, 7]))
print(remove_negative_element( [1, 2, 3, 4, 5]))