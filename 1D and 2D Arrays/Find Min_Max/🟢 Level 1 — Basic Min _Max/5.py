"""5. Find the Maximum in an Array of Negative Numbers
arr = [-5, -12, -3, -20, -8]
Find the maximum.
Think carefully about initialization."""

def maxi_negative_num(arr):
    max_num = float('-inf')
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num
print(maxi_negative_num([-5, -12, -3, -20, -8]))

#Time Complexity: O(n)
#Space Complexity: O(1)