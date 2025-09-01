# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If a number is a multiple of both 3 and 5, only count it once.

def multiplesOf3Or5(n):
  total = 0
  list3 = []
  list5 = []
  list3And5 = []
  result = []
  for i in range(n):
    if i%3 == 0:
      list3.append(i)
    if i%5 == 0:
      list5.append(i)
  
  for i in range(len(list3)):
    for j in range(len(list5)):
      if list3[i] == list5[j]:
        list3And5.append(list3[i])
  
  for i in range(len(list3)):
    result.append(list3[i])
  
  for i in range(len(list5)):
    result.append(list5[i])

  for i in range(len(list3And5)):
    result.remove(list3And5[i])

  for i in result:
    total += i
  
  return total

  

print(multiplesOf3Or5(15))