"""Problem 1: Move Zeroes (In-Place Manipulation)
Given an integer array nums, move all 0s to the end of it while 
maintaining the relative order of the non-zero elements.
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Constraints: You must do this in-place without making a copy of the array.
Coach's Challenge: Minimize the total number of write operations 
instead of blindly swapping every element."""
#Brute Force 
def move_zeroes(nums):
    li = []
    for i in range(len(nums)):
        if nums[i] != 0:
            li.append((nums[i]))
    sub_zeroes = len(nums) - len(li)
    for i in range(sub_zeroes):
        li.append((0))    
    return li
print(move_zeroes([0, 1, 0, 3, 12]))
#print(move_zeroes([1, 2, 3, 4]))
#print(move_zeroes([0, 0, 0]))
#print(move_zeroes([1, 0, 2, 0, 3]))
#print(move_zeroes([-1, 0, -2, 3, 0])

# In-Place Manipulation using same direction pointer
def move_zeroes(nums):
    fast = 0
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            if fast != slow: # <-- The micro-optimization
                nums[slow] = nums[fast]
            slow += 1
    diff = len(nums) - slow
    for i in range(diff):
        nums[slow] = 0
        slow += 1
    return nums
print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([-1, 0, -2, 3, 0]))
print(move_zeroes([1, 2, 3]))

#Time complexity = O(n)
#Space Complexity = O(1)



        
