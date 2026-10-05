"""Problem 1: Find an Element
Given a sorted array:
nums = [2, 5, 8, 12, 16, 23, 38, 45, 56]
target = 23
Find the index of target using binary search.
output : 5
"""
def binary_search(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high) // 2
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess> target:
            high = mid-1
        else:
            low = mid + 1
    return None
print(binary_search([2, 5, 8, 12, 16, 23, 38, 45, 56], 23))
            
"""Your code's complexity
- Time: O(log n) ✅
- Space: O(1) ✅
"""