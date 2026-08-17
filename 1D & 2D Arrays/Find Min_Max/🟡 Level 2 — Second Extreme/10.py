"""### 10. Find Largest and Second Largest Together
arr = [4, 17, 9, 12, 3, 21, 8]
Find:
largest
secondLargest
using exactly one traversal.After solving, explain when `secondLargest` needs to change."""

def largest_secondlargest(arr):
    largest = float('-inf')
    secondLargest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] > secondLargest:
            secondLargest = arr[i]
    return largest, secondLargest
print(largest_secondlargest([4, 17, 9, 12, 3, 21, 8]))    
print(largest_secondlargest([21, 21, 17]))    

#Time Complexity: O(n)
#Space Complexity: O(1)