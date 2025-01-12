# Find the number with the most digits.

# If two numbers in the argument array have the same number of digits, return the first one in the array.

def findLongest(array):
  longestNumber = -1
  
  for i in array:
    numberLength = 0
    tempI = i
    while tempI > 0:
      numberLength += 1
      tempI /= 10
    if numberLength > longestNumber:
      longestNumber = i

  return longestNumber

print(findLongest([1, 10, 100]))