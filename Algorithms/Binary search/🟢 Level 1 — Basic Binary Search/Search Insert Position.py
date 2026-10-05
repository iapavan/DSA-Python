"""Problem 5 — Search Insert Position
Given a sorted array:
nums = [1, 3, 5, 6]
Find the index where target exists.
If it doesn't exist, return the position where it should be inserted.
Examples:
target = 5 → 2
target = 2 → 1
target = 7 → 4
target = 0 → 0
"""
def insert_positions(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high) // 2
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return low
print(insert_positions([1, 3, 5, 6],  2))
print(insert_positions([1, 3, 5, 6],  1))
print(insert_positions([1, 3, 5, 6],  4))
print(insert_positions([1, 3, 5, 6],  0))

        