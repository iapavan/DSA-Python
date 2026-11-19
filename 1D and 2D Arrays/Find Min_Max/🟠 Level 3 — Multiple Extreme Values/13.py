"""### 13. Find the Three Largest Distinct Values
arr = [10, 4, 20, 15, 8, 25, 20, 18]
Find:
largest
secondLargest
thirdLargest
You may maintain only a constant number of variables."""

def three_largest_distnt_val(arr):
    largest = float('-inf')
    secondLargest = float('-inf')
    thirdLargest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            thirdLargest = secondLargest
            secondLargest = largest 
            largest = arr[i]
        elif arr[i] > secondLargest and arr[i] != largest:
             thirdLargest = secondLargest
             secondLargest = arr[i]
        elif arr[i] > thirdLargest and  arr[i] != secondLargest and arr[i] != largest:
             #thirdLargest = secondLargest
             thirdLargest = arr[i]
    return largest, secondLargest, thirdLargest
print(three_largest_distnt_val([10, 4, 20, 15, 8, 25, 20, 18]))

#Time Complexity: O(n)
#Space Complexity: O(1)