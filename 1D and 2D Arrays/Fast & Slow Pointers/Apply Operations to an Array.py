"""
🟢 LEVEL 1 — BASIC
Problem Number: 3
Problem Title: Apply Operations to an Array
Difficulty: Basic
Problem Statement
You are given a 0-indexed array nums of size n 
consisting of non-negative integers.
Example 1
Input: nums = [1, 2, 2, 1, 1, 0]
Output: [1, 4, 2, 0, 0, 0]
"""

def array_operations(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i]*2
            nums[i+1] = 0 #assignment
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
    return  nums
print(array_operations([1, 2, 2, 1, 1, 0]))

#more Optimized version 
def array_operations(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i]*2
            nums[i+1] = 0 #assignment
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
           nums[slow], nums[fast] = nums[fast], nums[slow]
           slow += 1
    return  nums
print(array_operations([1, 2, 2, 1, 1, 0]))

"""
📊 Correctness percentage: 100%
⏱️ Time complexity: O(n) — three sequential passes over the array O(2n) simplifies to O(n).
💾 Space complexity: O(1) — modified completely in-place.
"""
