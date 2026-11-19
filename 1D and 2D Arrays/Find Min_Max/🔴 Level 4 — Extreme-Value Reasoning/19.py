"""### 19. Find the Two Extreme Pairs
Given:
arr = [12, 5, 18, 3, 9, 21, 7, 2]
Find:
smallest
secondSmallest
largest
secondLargest
using one traversal and O(1) extra space.
This is a very good test of whether you understand how multiple pieces of state can be maintained simultaneously."""

def two_extreme_pairs(arr):
    smallest = float('inf')
    secondSmallest = float('inf')
    largest = float('-inf')
    secondLargest = float('-inf')
    for i in range(len(arr)):
        if arr[i] < smallest:
            secondSmallest = smallest
            smallest = arr[i]
        elif arr[i] < secondSmallest and arr[i] != smallest:
            secondSmallest = arr[i]
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return  smallest,secondSmallest, largest, secondLargest
print(two_extreme_pairs([14, 6, 2, 19, 8, 4, 11]))