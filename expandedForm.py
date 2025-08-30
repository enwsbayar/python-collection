# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"
# NOTE: All numbers will be whole numbers greater than 0.

def expandedForm(num):
  result = ""
  length = len(str(num))  
  while(num != 0):
    result += str(num)[0] 
    result += "0"*(length-1)
    if(length-1 != 0):
      result += " + " 
    num = num % 10**(length-1)
    length = len(str(num))
  return result

print(expandedForm(12))