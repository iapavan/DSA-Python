"""🟡 Problem 4 — Last Occurrence
Given:
nums = [1, 2, 2, 2, 5, 7, 9]
target = 2
Find the last index where 2 occurs.
output = 3
"""
def last_occurrence(nums, target):
    low = 0
    high = len(nums)-1
    last = -1
    while low <= high:
        mid = (low+high)//2
        guess = nums[mid]
        if guess == target:
            last = mid
            low = mid + 1
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return last
print(last_occurrence([1, 2, 2, 2, 5, 7, 9], 2))

"""
complexity:
Time: O(log n)
Space: O(1)
"""
