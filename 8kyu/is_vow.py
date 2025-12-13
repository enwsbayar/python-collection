# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

# If they are, change the array value to a string of that vowel.

# input [100,100,116,105,117,121]=>[100,100,116,"i","u",121] output Return the resulting array.

def is_vow(inp):
  vowels = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
  return [vowels.get(x, x) for x in inp]

