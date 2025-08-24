# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def reverseString(string):
  result = ''
  length = len(string)
  for i in range(1, length + 1):
    i *= -1
    result += string[i]
  return result

print(reverseString('world'))


