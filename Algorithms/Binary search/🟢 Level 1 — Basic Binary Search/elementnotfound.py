"""🟢 Problem 2 — Element Not Present
nums = [3, 7, 11, 15, 20, 26, 31, 42]
target = 18
Return the index if the target exists; otherwise return:
output = -1
"""
def element_not_present(nums, target):
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
    return -1
print(element_not_present([3, 7, 11, 15, 20, 26, 31, 42], 18)) 

"""And complexity is:
Time: O(log n)
Space: O(1)
"""