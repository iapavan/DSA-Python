"""Problem Statement
Given an integer array nums and an integer val, remove all 
occurrences of val from the array in-place.
You do not need to preserve the elements beyond the new valid length.
Return the number of elements remaining after removing val.
nums = [3, 2, 2, 3]
val = 3
output : 2
"""
def remove_element(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            if fast != slow:
                nums[slow] = nums[fast]
            slow += 1
    return  slow
print(remove_element([3, 2, 2, 3], 3))