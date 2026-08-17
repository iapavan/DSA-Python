"""### 8. Second Maximum with Duplicates
arr = [10, 20, 20, 5, 15, 20]
Find the second largest distinct value
Question:
Should another `20` become your `secondLargest`?
Explain why."""
def second_maxi(arr):
    largest = float('-inf')
    secondLargest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    return largest, secondLargest
print(second_maxi([10, 20, 20, 5, 15, 20]))

#Time Complexity: O(n)
#Space Complexity: O(1)