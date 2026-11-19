"""### 6. Find the Second Maximum
arr = [10, 5, 8, 20, 15]
Find the second largest distinct value using one traversal.
You need to maintain:
largest = ?
secondLargest = ?
"""

def second_max(arr):
    largest = float('-inf')
    secondLargest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest =  arr[i]
        elif arr[i] > secondLargest  and arr[i] != largest:
           # largest = secondLargest
            secondLargest = arr[i]    
    return largest, secondLargest
print(second_max([10, 5, 8, 20, 15]))
print(second_max([10, 20, 5]))
print(second_max([20, 20, 10]))   

#Time Complexity: O(n)
#Space Complexity: O(1)