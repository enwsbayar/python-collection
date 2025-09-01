# Task
# You get an array of numbers, return the sum of all of the positives ones.

# Example
# [1, -4, 7, 12] => 
# 1+7+12=20

# Note

# If there is nothing to sum, the sum is default to 0.

def positiveSum(arr):
  result = 0
  for i in arr:
    if i > 0:
      result += i
  return result

print(positiveSum([1, -4, 7, 12]))