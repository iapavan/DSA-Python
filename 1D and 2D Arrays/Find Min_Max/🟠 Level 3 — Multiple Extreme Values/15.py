"""### 15. Find the Range
arr = [7, 2, 15, 4, 10, 1]
Find:
maximum - minimum
using one traversal.
Key question:
Do you need to store the entire array?
"""

def find_range_arr(arr):
    range_arr = 0
    maxi = float('-inf')
    mini = float('inf')
    for i in range(len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
        if arr[i] < mini:
            mini = arr[i]
    range_arr = maxi - mini
    return range_arr
print(find_range_arr([7, 2, 15, 4, 10, 1]))

#Time Complexity: O(n)
#Space Complexity: O(1)