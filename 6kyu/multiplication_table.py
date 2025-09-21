# Your task, is to create N×N multiplication table, of size provided in parameter.

# For example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:

# [[1,2,3],[2,4,6],[3,6,9]]

def multiplication_table(n):
  return [[i*j for j in range(1, n+1)] for i in range(1, n+1)]

print(multiplication_table(3))