# Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.

# Ex:

# 274 -> '2-7-4'
# 6815 -> '68-1-5'

def dashatize(n):
  if n is None:
      return None
  s = str(abs(int(n)))
  res = []
  for i, ch in enumerate(s):
    d = int(ch)
    if d % 2 == 1:
      if res and res[-1] != '-':
        res.append('-')
      res.append(ch)
      if i != len(s) - 1:
        res.append('-')
    else:
      res.append(ch)
  return ''.join(res).strip('-')