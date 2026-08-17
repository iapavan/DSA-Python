"""### 16. Find the Minimum and Maximum Difference
Given:
arr = [10, 3, 8, 20, 5, 2]
Find the difference between the largest and smallest elements.
Then explain why this is still:
Time: O(n)
Space: O(1)
"""

def mini_maxi_diff(arr):
    mini_num = float('inf')
    maxi_num = float('-inf')
    diff_num = 0
    for i in range(len(arr)):
        if arr[i] > maxi_num:
            maxi_num = arr[i]
        if arr[i] < mini_num:
            mini_num = arr[i]
    diff_num = maxi_num - mini_num
    return diff_num
print(mini_maxi_diff([10, 3, 8, 20, 5, 2]))

"""The "Why" Behind the ComplexitiesIn Data Structures and Algorithms, we use Big-O notation to describe how an algorithm scales as the amount of data (the size of the array, represented by $n$) grows.1. Time Complexity: $O(n)$ (Linear Time)Time complexity measures how many operations the computer has to perform relative to the size of the input.In all of your optimized solutions, you rely on a single for i in range(len(arr)): loop.This means you traverse the array exactly one time.The number of steps the computer takes scales perfectly proportionally with the data. If the array size grows to 1 million, your loop runs exactly 1 million times. Because it forms a straight line on a graph, we call this "linear time" or $O(n)$.2. Space Complexity: $O(1)$ (Constant Space)Space complexity does not measure the size of the array itself; it measures how much extra or additional memory your algorithm needs to run.Before your loop starts, you create a strictly limited number of tracking variables (like smallest and secondSmallest).You only created two variables to store your answers.It does not matter how massive the array gets; you still only need those two small blocks of memory. Because the extra memory requirement never grows, it remains "constant," which is written as $O(1)$.To help you visualize this mathematical scaling, here is an interactive chart. Adjust the array size to see exactly how $O(n)$ time grows while $O(1)$ space remains completely flat!"""