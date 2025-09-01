# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

def high(x):
  resultList = []
  total = 0
  for letter in x:
    if letter == " ":
      resultList.append(total)
      total = 0
    else:
      total += ord(letter)-ord("a")+1
  
  if total > 0:
    resultList.append(total)
    
  maxNumberIdx = resultList.index(max(resultList))
  words = x.split(" ")
  return words[maxNumberIdx]

print(high('man i need a taxi up to ubu'))