# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# For example:

# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6 (Sum of [4, -1, 2, 1])
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead. Your solution should be fast, it will be tested on very large arrays so slow solutions will time out.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    """
    Kadane's Algorithm to find maximum sum of contiguous subarray.
    Time Complexity: O(n), Space Complexity: O(1)
    """
    if not arr:
        return 0
    
    max_current = max_global = 0
    
    for num in arr:
        max_current = max(0, max_current + num)
        max_global = max(max_global, max_current)
    
    return max_global

