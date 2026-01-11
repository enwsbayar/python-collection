# Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

# (the dedicated builtin(s) functionalities are deactivated)

def reverse(lst):
  result = list()
  for i in range(len(lst) - 1, -1, -1):
    result.append(lst[i])
  return result