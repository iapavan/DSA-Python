"""Your first challenge 🧠
Don't think about optimization yet.
Imagine you had to solve this in the most straightforward way possible.
For:
arr = [1, 2, 3, 4, 5]
output = [4, 5, 1, 2, 3]
k = 2"""
#Brute Force
def rotate_array(arr, k):
    res = []
    for i in range(len(arr)-k,len(arr)):
       res.append(arr[i])   
    for i in range(len(arr)-k):
        res.append(arr[i])     
    return res
#print(rotate_array([1, 2, 3, 4, 5], 2))
print(rotate_array([1,2,3,4,5,6,7], 3))

"""Time complexity
You traverse:
B → k elements
A → n-k elements
Total:
k + (n-k)= n
Therefore:
Time = O(n) ✅
Space complexity
You create:
res = []
and put all n elements into it.
Therefore:
Extra space = O(n) ✅
So your brute-force approach is:
| Approach            |     Time |    Space |
| ------------------- | -------: | -------: |
| Your `res` approach | **O(n)** | **O(n)** |

"""
def rotate_array(arr, k):
    l = 0
    r = len(arr)-k-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    l = len(arr)-k
    r = len(arr)-1
    while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    l = 0
    r = len(arr)-1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr
#print(rotate_array([1, 2, 3, 4, 5], 2))
print(rotate_array([1,2,3,4,5,6,7], 3))
