# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

# If the array is invalid (empty, or contains negative integers or integers with more than 1 digit), return nil (or your language's equivalent).

# Examples
# Valid arrays

# [4, 3, 2, 5] would return [4, 3, 2, 6] (4325 + 1 = 4326)
# [1, 2, 3, 9] would return [1, 2, 4, 0] (1239 + 1 = 1240)
# [9, 9, 9, 9] would return [1, 0, 0, 0, 0] (9999 + 1 = 10000)
# [0, 1, 3, 7] would return [0, 1, 3, 8] (0137 + 1 = 0138)
# Invalid arrays

# [] is invalid because it is empty
# [1, -9] is invalid because -9 is not a non-negative integer
# [1, 2, 33] is invalid because 33 is not a single-digit integer

def up_array(arr):
    # Check if array is invalid
    if not arr or any(x < 0 or x > 9 for x in arr):
        return None
    
    # Create a copy to work with
    result = arr.copy()
    
    # Add 1 starting from the rightmost digit
    carry = 1
    for i in range(len(result) - 1, -1, -1):
        result[i] += carry
        if result[i] == 10:
            result[i] = 0
            carry = 1
        else:
            carry = 0
            break
    
    # If there's still a carry, we need to add a digit at the front
    if carry == 1:
        result.insert(0, 1)
    
    return result