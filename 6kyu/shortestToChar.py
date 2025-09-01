# Given a string s and a character c, return an array of integers representing the shortest distance from the current character in s to c.

# Notes
# All letters will be lowercase.
# If the string is empty, return an empty array.
# If the character is not present, return an empty array.
# Examples
# s = "lovecodewars"
# c = "e"
# result = [3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4]

# s = "aaaabbbb"
# c = "b"
# result = [4, 3, 2, 1, 0, 0, 0, 0]

# s = ""
# c = "b"
# result = []

# s = "abcde"
# c = ""
# result = []

def shortestToChar(s, c):
  if not s or not c or c not in s:
      return []

  idxList = []
  for a, i in enumerate(s):
      if i == c:
          idxList.append(a)

  result = []
  for i in range(len(s)):
      minDist = min(abs(i - idx) for idx in idxList)
      result.append(minDist)

  return result
  
  
print(shortestToChar("lovecodewars", "e"))