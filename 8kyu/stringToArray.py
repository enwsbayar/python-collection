# Write a function to split a string and convert it into an array of words.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]

def stringToArray(s):
  return s.split(" ")
  

print(stringToArray("Robin Singh"))