"""### 18. Find the Second Smallest Without Sorting
arr = [14, 6, 2, 19, 8, 4, 11]
Same constraints.
❌ No sorting
❌ No second traversal
❌ No extra array
✅ One traversal
Find the second smallest."""

def second_smallest_num(arr):
    smallest = float('inf')
    secondSmallest = float('inf')
    for i in range(len(arr)):
        if arr[i] < smallest:
            secondSmallest = smallest
            smallest = arr[i]
        elif arr[i] < secondSmallest and arr[i] != smallest:
            secondSmallest = arr[i]
    return secondSmallest
print(second_smallest_num([14, 6, 2, 19, 8, 4, 11]))

#Time Complexity: O(n)
#Space Complexity: O(1)