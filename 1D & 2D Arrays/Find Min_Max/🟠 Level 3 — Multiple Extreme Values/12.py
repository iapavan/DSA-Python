"""### 12. Find the Two Largest Distinct Values
arr = [15, 7, 20, 20, 9, 13, 18]
Return:
largest
secondLargest
One traversal only."""

def two_largest_distnt_val(arr):
    largest = float('-inf')
    secondLargest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return largest, secondLargest
print(two_largest_distnt_val([15, 7, 20, 20, 9, 13, 18]))

#Time Complexity: O(n)
#Space Complexity: O(1)