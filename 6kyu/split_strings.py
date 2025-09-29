# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
  c1 = 0
  c2 = 1
  result = []  
  if (len(s)%2):
    s = s + "_"
  
  for c in range(len(s)//2):
    result.append(s[c1] + s[c2])
    c1 += 2
    c2 += 2

  return result

print(solution('abc'))