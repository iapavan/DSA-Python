"""### 20. Extreme Values with Edge Case:
Write an algorithm that finds the:
minimum
second minimum
maximum
second maximum
for an array.
Your algorithm must:
✅ Use one traversal
✅ Use O(1) extra space
❌ Not sort
❌ Not create another array
And decide what should happen for these cases:
[5]
[5, 5]
[5, 3]
[5, 5, 5]
[-10, -5, -20, -3]
[2, 1, 2, 1, 3]
The important part isn't just getting the answer.
You must explain your state/invariant:
After processing index `i`, what exactly do `min`, `secondMin`, `max`, and `secondMax` represent?"""

def two_extreme_pairs(arr):
    minimum = float('inf')
    secondminimum = float('inf')
    maximum = float('-inf')
    secondmaximum = float('-inf')
    for i in range(len(arr)):
        if arr[i] < minimum:
            secondminimum = minimum
            minimum = arr[i]
        elif arr[i] < secondminimum and arr[i] != minimum:
            secondminimum = arr[i]
        if arr[i] > maximum:
            secondmaximum = maximum
            maximum = arr[i]
        elif arr[i] > secondmaximum and arr[i] != maximum:
            secondmaximum = arr[i]
    return  minimum,secondminimum, maximum, secondmaximum
print(two_extreme_pairs([5]))
print(two_extreme_pairs([5, 5]))
print(two_extreme_pairs([5, 3]))
print(two_extreme_pairs([5, 5, 5]))
print(two_extreme_pairs([-10, -5, -20, -3]))
print(two_extreme_pairs([2, 1, 2, 1, 3]))

"""The Loop Invariant Explained
In computer science, a loop invariant is a condition or a "truth" that remains strictly true before and after every single iteration of your loop. It is the core proof that your algorithm works.
For your specific algorithm, the invariant is tied to the concept of a "subarray." As your loop moves forward, it is essentially looking at a growing slice of the data, from the very first element arr[0] up to the current element arr[i].
After your loop finishes processing index i, here is the absolute truth about your four variables:
minimum: It represents the absolute smallest value found strictly within the elements seen so far (arr[0] through arr[i]).
secondminimum: It represents the strictly second smallest distinct value found within the elements seen so far (arr[0] through arr[i]). If a second distinct value has not appeared yet, it remains exactly as initialized: positive infinity.
maximum: It represents the absolute largest value found strictly within the elements seen so far (arr[0] through arr[i]).
secondmaximum: It represents the strictly second largest distinct value found within the elements seen so far (arr[0] through arr[i]). If a second distinct value has not appeared yet, it remains exactly as initialized: negative infinity.
Why the Invariant Matters
By ensuring this specific truth holds up after index 0, then after index 1, then after index 2, you mathematically guarantee that when i reaches the very end of the array, your variables will accurately represent the extreme pairs for the entire dataset."""

#Time Complexity: O(n)
#Space Complexity: O(1)