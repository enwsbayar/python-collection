# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string

def is_valid_IP(strng):
  if strng.count(".") != 3:
      return False
  
  numbers = strng.split(".")
  
  for n in numbers:
    if not n.isdigit():
        return False
    
    if len(n) > 1 and n[0] == "0":
        return False
    
    if int(n) < 0 or int(n) > 255:
        return False
  
  return True

print(is_valid_IP("123.045.067.089"))