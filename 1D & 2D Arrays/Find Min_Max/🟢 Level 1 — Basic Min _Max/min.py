"""1. Find the Minimum
arr = [7, 3, 9, 2, 8, 5]
Find the smallest element using one traversal.
Think: What single piece of information must you maintain?"""
#Using nested loops
def mini(ar):
    min_num = float('inf')
    for i in range(len(ar)):
        for j in range(len(ar)):
            if ar[j] < min_num:
                min_num = ar[j]
    return min_num
#print(mini([7, 3, 9, 2, 8, 5]))
#Time Complexity O(n)^2
"for j in range(i+1, len(ar)+1):"

def mini(ar):
    min_num = float('inf')
    for i in range(len(ar)):
        if ar[i] < min_num:
                min_num = ar[i]
    return min_num
print(mini([7, 3, 9, 2, 8, 5]))
#Time Complexity O(n)