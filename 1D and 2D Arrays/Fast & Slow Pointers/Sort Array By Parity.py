"""🟢 LEVEL 1 — BASIC
Problem Number: 2
Problem Title: Sort Array By Parity
Difficulty: Basic
Problem Statement
Given an integer array nums, move all the even integers to the beginning 
of the array followed by all the odd integers.
Example 1
Input: nums = [3, 1, 2, 4]
Output: [2, 4, 3, 1]
(Explanation: The outputs [4, 2, 3, 1], [2, 4, 1, 3], 
and [4, 2, 1, 3] would also be accepted.)
Example 2
Input: nums = [0]
Output: [0]
"""
#Brute Force
def sort_array(nums):
    evn_li = []
    od_li = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            evn_li.append(nums[i])
        else:
            od_li.append(nums[i])
    return evn_li+od_li
print(sort_array([3, 1, 2, 4]))
"""
Complexity 🧠
Your solution is Brute Force / auxiliary-array approach:
Time: O(n) — you visit every element once.
Space: O(n) — you create two additional lists.
"""
#In-place using O(1) extra space
def sort_array(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] % 2 == 0:
            if fast != slow:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums
nums = [3, 1, 2, 4]
k = sort_array(nums)
print(k)

"""📊Correctness percentage: 100%
⏱️Time complexity: O(n) — single pass through the array.
💾Space complexity: O(1) — modified in-place with zero extra memory.
"""           