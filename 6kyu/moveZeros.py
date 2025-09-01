# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def moveZeros(list):

  counter = 0
  zeroCounter = list.count(0)

  while counter < len(list):

    if list[counter] == 0:
      list.pop(counter)
    else:
      counter += 1

  for i in range(zeroCounter):
    list.append(0)

  return list

print(moveZeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))