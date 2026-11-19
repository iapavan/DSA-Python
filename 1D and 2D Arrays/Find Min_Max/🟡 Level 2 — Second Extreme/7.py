"""### 7. Find the Second Minimum
arr = [10, 5, 8, 20, 2, 15]
Find the second smallest distinct value.
Maintain:
smallest = ?
secondSmallest = ?
"""

def second_mini(arr):
    smallest = float('inf')
    secondSmallest = float('inf')
    for i in range(len(arr)):
        if arr[i] < smallest:
            secondSmallest = smallest
            smallest = arr[i]
        elif arr[i] < secondSmallest and arr[i] != smallest:
            secondSmallest = arr[i]
    return smallest, secondSmallest
print(second_mini([10, 5, 8, 20, 2, 15]))
print(second_mini([15, 22, 8, 99, 4, 42]))
print(second_mini([100, 50, 20, 10, 5]))
print(second_mini([5, 10, 20, 50, 100]))
print(second_mini([100, 100, 50, 50, 10, 10]))
print(second_mini([-1, -50, -2, -100, -25]))
print(second_mini([7, 3]))

#Time Complexity: O(n)
#Space Complexity: O(1)

