"""2. Find the Maximum
arr = [7, 3, 9, 2, 8, 5]
Find the largest element using **one traversal**.
Maintain:""" 

def maxi_num(arr):
    max_num = float('-inf')
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num
print(maxi_num([7, 3, 9, 2, 8, 5]))

#Time Complexity: O(n)
#Space Complexity: O(1)
        