"""Exercise 1: Right Rotate by k Steps (The Standard)Given an integer array nums and a non-negative integer k, rotate the array to the right by k steps.
Example 1:Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Explanation:1 step right: [7, 1, 2, 3, 4, 5, 6]
            2 steps right: [6, 7, 1, 2, 3, 4, 5]
            3 steps right: [5, 6, 7, 1, 2, 3, 4]
Example 2:Input: nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
Constraints: 
Challenge: Can you do this in-place with O(1) extra memory"""

#without in-place
def right_rotate_by_k_steps(arr, k):
    n = len(arr)
    res =[]
    for i in range(n-k, n):
        res.append(arr[i])
        #print(res)
    for i in range(n-k):
        res.append(arr[i])
        print(res)
    return res
#print(right_rotate_by_k_steps([1, 2, 3, 4, 5, 6, 7], 3))

#with in-place with O(1) extra memory

def right_rotate_by_k_steps(arr, k):
    n = len(arr)
    l = 0
    r = n-k-1
    while l < r :
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    l = n-k
    r = n-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    l = 0
    r = n-1
    while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return arr
print(right_rotate_by_k_steps([1, 2, 3, 4, 5, 6, 7], 3))
print(right_rotate_by_k_steps([-1, -100, 3, 99], 2))
print(right_rotate_by_k_steps([1, 2], 3))

