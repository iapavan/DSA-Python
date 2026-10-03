"""1. Remove Duplicates from Sorted Array
Input:
nums = [1,1,2,2,3,4,4]
Output:
[1,2,3,4]"""

#Brute Force 
def remove_duplicates(nums):
    my_set = set() #intialization
    for i in range(len(nums)):
        my_set.add(nums[i]) #Adding element to set 
    return my_set
print(remove_duplicates([1,1,2,2,3,4,4]))

"""
Complexity of your approach
Time: O(n)
You visit every element once.
Space: O(n)
The set can contain up to n unique elements.
"""

#in-place using slow and fast pointer
def remove_duplicates(nums):
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow-1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
#print(remove_duplicates([1,1,2,2,3,4,4]))
nums = [1, 1, 2, 2, 3, 4, 4]

k = remove_duplicates(nums)

print(nums[:k])
print("Number of unique elements:", k)

"""
Time: O(n)
Extra space: O(1)
"""