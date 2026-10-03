#Reversing an array in-place
def reverse_arr(arr):
    l = 0
    r = len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l] 
        l += 1
        r -= 1
    return arr
        
print(reverse_arr([10, 20, 30, 40, 50, 60]))
print(reverse_arr([1,2,3,4,5,6]))

"""🧠 You discovered the algorithm

The important pattern is:

L = beginning
R = end

while L < R:
    swap(L, R)
    L → right
    R → left
The deeper idea

You aren't really "moving elements."

You're repeatedly fixing two positions at a time:

first  ↔ last
second ↔ second-last
third  ↔ third-last
...

Once L and R cross, every position is already correct.

Complexity

For an array of n elements:

Time: O(n) — roughly n/2 swaps
Extra space: O(1) — only the two pointers and temporary swap storage
In-place: ✅
Pattern: Two Pointers"""