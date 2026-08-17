"""### 14. Find the Three Smallest Distinct Values
arr = [12, 3, 7, 1, 9, 3, 5, 2]
Find the three smallest distinct values.
Think:
smallest
secondSmallest
thirdSmallest
"""

def three_smallest_distnt_vals(arr):
    smallest = float('inf')
    secondSmallest = float('inf')
    thirdSmallest = float('inf')
    for i in range(len(arr)):
        if arr[i] < smallest:
            thirdSmallest = secondSmallest
            secondSmallest = smallest
            smallest = arr[i]
        elif arr[i] < secondSmallest and arr[i] != smallest:
            thirdSmallest = secondSmallest
            secondSmallest = arr[i]
        elif arr[i] < thirdSmallest and arr[i] != smallest and arr[i] != secondSmallest:
            thirdSmallest = arr[i]
    return smallest, secondSmallest, thirdSmallest

print(three_smallest_distnt_vals([12, 3, 7, 1, 9, 3, 5, 2]))

#Time Complexity: O(n)
#Space Complexity: O(1)
    