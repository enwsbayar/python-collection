# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

# The input will be a lowercase string with no spaces.

# Good luck!

def capitalize(s): 
  return [''.join(c.upper() if i%2==0 else c for i,c in enumerate(s)), ''.join(c.upper() if i%2 else c for i,c in enumerate(s))]

print(capitalize("abcdef"))