"""Remove Element: Given an array and a value, remove all instances 
of that specific value in-place and return the new length.
Input: nums = [3, 2, 2, 3], val = 3
Output: 2, nums = [2, 2, _, _]
"""
#Brute Force 
def remove_element(nums, val):
    li = []
    for i in range(len(nums)):
        if nums[i] != val:
            li.append(nums[i])
    return len(li), li
print(remove_element([3, 2, 2, 3], 3))

#specific value in-place using the same direction pointer
def remove_element(nums, val):
    fast = 0
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            if fast != slow:
                nums[slow] = nums[fast]
            slow += 1
    return slow, nums
print(remove_element([3, 2, 2, 3], 3))
