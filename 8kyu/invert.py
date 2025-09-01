# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []
# You can assume that all values are integers. Do not mutate the input array.

def invert(lst):
  lstT = lst.copy()
  for idx,num in enumerate(lstT):
    lstT[idx] *= -1
  return lstT

print(invert([1, -2, 3, -4, 5]))