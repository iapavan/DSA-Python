"""🟡 Problem 3 — First Occurrence
Given:
nums = [1, 2, 2, 2, 5, 7, 9]
target = 2
Find the first index where 2 occurs.
output : 1
💡 This is where binary search starts becoming more interesting.
"""
def first_occurrence(nums, target):
    low = 0
    high = len(nums)-1
    first = -1
    while low <= high:
        mid = (low+high)//2
        guess = nums[mid]
        if guess == target:
            first = mid
            high = mid-1
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return first
print(first_occurrence([1, 2, 2, 2, 5, 7, 9], 2))
