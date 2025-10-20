# You are given an input (n) which represents the amount of lines you are given, your job is to figure out what is the maximum amount of perpendicular lines you can make using these lines.

# Note: A perpendicular line is one that forms a 90 degree angle

# n will always be greater than or equal to 0
def perpendicular(n):
  return (n // 2) * (n - n // 2)