"""### 4. Find the Minimum in an Array of Negative Numbers
arr = [-5, -12, -3, -20, -8]
Find the minimum.
**Important:** What should your initial value be?""" 

def mini_negative_num(arr):
    mini_num = float('inf')
    for i in range(len(arr)):
        if arr[i] < mini_num:
            mini_num = arr[i]
    return mini_num
print(mini_negative_num([-5, -12, -3, -20, -8]))

#Time Complexity: O(n)
#Space Complexity: O(1)