""" 3. Find Both Minimum and Maximum
arr = [12, 5, 8, 1, 19, 4]
Find both the minimum and maximum in a **single traversal**.
Think
min = ?
max = ?"""

def min_max_nums(ar):
    min_num = float('inf')
    max_num = float('-inf')
    for i in range(len(ar)):
        if ar[i]<min_num:
            min_num = ar[i]
        if ar[i]>max_num:
            max_num = ar[i]
    return min_num, max_num
print(min_max_nums([12, 5, 8, 1, 19, 4]))