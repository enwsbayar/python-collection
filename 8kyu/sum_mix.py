# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

def sum_mix(arr):
  return  sum(int(i) for i in arr)

print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))