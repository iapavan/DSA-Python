"""
Level 1 – Basic
Problem 1: Remove a Specific Element
Given an array, remove all occurrences of 2 in-place.
Input:
nums = [3, 2, 2, 3, 4, 2, 5]
val = 2
Output:
Return absolute new length
[3, 3, 4, 5]
"""
def remove_specific_val(nums, val):
    #fast = 0
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            if fast != slow:
                nums[slow] = nums[fast]
            slow += 1
    """
     diff = len(nums) - slow
        for i in range(diff):
            nums.pop(slow) 
         this is the physical removal of the element but we want the logical removal
    """
   
    return slow
print(remove_specific_val([3, 2, 2, 3, 4, 2, 5], 2))
print(remove_specific_val([1, 2, 2, 3, 4, 2], 2))

#Try it independently. Don't use pop() this time. Return the new length (slow).