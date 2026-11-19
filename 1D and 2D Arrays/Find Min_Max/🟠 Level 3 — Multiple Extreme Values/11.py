"""### 11. Find the Two Smallest Distinct Values
arr = [8, 3, 12, 2, 5, 2, 9]
Return:
smallest
secondSmallest
Both must be distinct."""

def two_smallest_distnt_val(arr):
    smallest = float('inf')
    secondSmallest = float('inf')
    for i in range(len(arr)):
        if arr[i] < smallest:
            secondSmallest = smallest
            smallest = arr[i]
        elif arr[i] < secondSmallest and arr[i] != smallest:
            secondSmallest = arr[i]
    return smallest, secondSmallest
print(two_smallest_distnt_val([8, 3, 12, 2, 5, 2, 9]))

#Time Complexity: O(n)
#Space Complexity: O(1)