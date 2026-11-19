"""Problem 3: Move Even Numbers First
Move all even numbers to the beginning, maintaining the relative 
order of even numbers and odd numbers.
Input:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
output:
[2, 4, 6, 8, 1, 3, 5, 7]
Challenge: In-place, with minimum writes.
"""
def move_even_numbers_first(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] % 2 == 0:
            if fast != slow:
                even_val = nums[fast]
                # Shift the odd numbers between slow and fast-1 one step right
                for j in range(fast, slow, -1):
                    nums[j] = nums[j-1]
                nums[slow]=even_val
            slow += 1
    
    return nums
print(move_even_numbers_first([1, 2, 3, 4, 5, 6, 7, 8]))
"""
Time complexity : O(n^2) in worst case
Space complexity : O(1) strictly in-place
"""
def move_even_numbers_first(nums):
    slow = 0
    odds = []
    for fast in range(len(nums)):
        if nums[fast]%2 != 0:
            odds.append(nums[fast])
        else:
            if fast != slow:
                nums[slow] = nums[fast]
            slow += 1
    for val in odds:
        nums[slow] = val
        slow += 1
    return nums
print(move_even_numbers_first([1, 2, 3, 4, 5, 6, 7, 8]))
                