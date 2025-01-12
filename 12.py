# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)


def isIsogram(string):
  string = string.lower()
  total = 0
  for i in string:
    for j in string:
      if i == j:
        total += 1

  if total > len(string):
    return False
  else:
    return True
  
print(isIsogram("moOse"))