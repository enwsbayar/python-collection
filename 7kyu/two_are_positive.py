# Task:
# Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of the three integers are positive numbers (greater than zero), and False - otherwise.

# Examples:
# two_are_positive(2, 4, -3) == True
# two_are_positive(-4, 6, 8) == True
# two_are_positive(4, -6, 9) == True
# two_are_positive(-4, 6, 0) == False
# two_are_positive(4, 6, 10) == False
# two_are_positive(-14, -3, -4) == False

def two_are_positive(a, b, c): 
  return sum(x > 0 for x in (a, b, c)) == 2

print(two_are_positive(4, 6, 10))