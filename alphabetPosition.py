# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# Input = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


def alphabetPosition(text):
  alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alphabet2 = "abcdefghijklmnopqrstuvwxyz"
  result = ""
  length = len(text)
  for i in range(length):
    if text[i].isupper():
      result += str(alphabet1.index(text[i]) + 1)
      result += " "
    
    if text[i].islower():
      result += str(alphabet2.index(text[i]) + 1)
      result += " "
  return result
    
  
  
print(alphabetPosition("The sunset sets at twelve o' clock."))