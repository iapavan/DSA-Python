"""🟢 LEVEL 1 — BASIC
Problem Number: 4
Problem Title: Sort Array By Parity II
Difficulty: Basic
Problem Statement
Given an array of integers nums, half of the integers in nums are odd,
and the other half are even.Sort the array in-place so that whenever 
nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return the modified array nums. (Any valid arrangement that satisfies the condition is accepted).
Example 1
Input: nums = [4, 2, 5, 7]
Output: [4, 5, 2, 7]
(Explanation: [4, 7, 2, 5], [2, 5, 4, 7], and [2, 7, 4, 5] are also accepted because indices 0 and 2 have even numbers, and indices 1 and 3 have odd numbers.)
"""
def sort_array(nums):
    odd_ptr= 1
    for even_ptr in range(0, len(nums), 2):
        if nums[even_ptr]%2 == 1:
            while nums[odd_ptr] % 2 == 0:
                  nums[odd_ptr], nums[even_ptr] = nums[even_ptr], nums[odd_ptr]
                  odd_ptr += 2
            
    return nums
nums = [4, 2, 5, 7]
k = sort_array(nums)
print(k)
            