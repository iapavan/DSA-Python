"""### 17. Find the Second Largest Without Sorting
arr = [5, 17, 3, 12, 9, 21, 8]
Constraints:
❌ No sorting
❌ No second traversal
❌ No extra array
✅ One traversal
Find the second largest.
Explain exactly when your two variables change."""

def second_largest(arr):
    largest = float('-inf')
    secondLargest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return secondLargest
print(second_largest([5, 17, 3, 12, 9, 21, 8])) 

#Time Complexity: O(n)
#Space Complexity: O(1)
#Explain exactly when your two variables change.
"Here why we need two variables to find secondlargest for that first we have find the frist largest number then only we can find the second largest number"        