# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2):

  if len(s1) <= len(s2):
    shortLength = len(s1)
    shortWord = s1
    longWord = s2
  else:
    shortLength = len(s2)
    shortWord = s2
    longWord = s1

  for i in range(shortLength):
    if shortWord.count(shortWord[i]) <= longWord.count(shortWord[i]):
      pass
    else:
      return False
    
  return True

print(scramble('scriptingjava', 'javascript'))


