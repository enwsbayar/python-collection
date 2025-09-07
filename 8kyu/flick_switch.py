# Task
# Create a function that always returns True/true for every item in a given list.
# However, if an element is the word 'flick', switch to always returning the opposite boolean value.

# Examples
# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]

def flick_switch(lst):
  flag = True
  return [(flag := not flag) if x == "flick" else flag for x in lst]

print(flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))