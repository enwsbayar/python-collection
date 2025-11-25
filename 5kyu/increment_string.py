# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng):
  if not strng:
    return "1"
  
  i = len(strng) - 1
  while i >= 0 and strng[i].isdigit():
    i -= 1
  
  text_part = strng[:i+1]
  num_part = strng[i+1:]
  
  if not num_part:
    return text_part + "1"
  
  num_length = len(num_part)
  incremented = str(int(num_part) + 1)
  
  if len(incremented) > num_length:
    return text_part + incremented
  else:
    return text_part + incremented.zfill(num_length)