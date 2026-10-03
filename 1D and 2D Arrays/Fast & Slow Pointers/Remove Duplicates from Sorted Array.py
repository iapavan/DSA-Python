"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.
example-1:
Input: nums = [1, 1, 2]

Output: 2, nums = [1, 2, _]
example-2:
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
"""
def remove_duplicate(nums):
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow-1]:
            if fast != slow:
                nums[slow] = nums[fast]
            slow += 1
        
    return slow
#nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1,2,3,4]
k = remove_duplicate(nums)
print(nums[:k])
                     
"""⏱️ Time complexity: O(n) — fast traverses the array of length n exactly once, 
doing O(1) work per step.
💾 Space complexity: O(1) — all modifications happen in-place using only two pointer variables."""