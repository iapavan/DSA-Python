"""### 9. Second Minimum with Duplicates
arr = [3, 1, 1, 7, 5, 3]
Find the second smallest distinct value.
Think about the difference between:
secondsmallest and secondsmallestdistinct"""

def second_mini(arr):
    secondsmallest = float('inf')
    secondsmallestdistinct = float('inf')
    for i in range(len(arr)):
        if arr[i] < secondsmallest:
            secondsmallestdistinct = secondsmallest
            secondsmallest = arr[i]
        elif arr[i] < secondsmallestdistinct and arr[i] != secondsmallest:
            secondsmallestdistinct = arr[i]
    return secondsmallest, secondsmallestdistinct

print(second_mini([3, 1, 1, 7, 5, 3]))

#Time Complexity: O(n)
#Space Complexity: O(1)