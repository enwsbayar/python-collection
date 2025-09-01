# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def breakCamelCase(s):
  result = []
  for ch in s:
      if ch.isupper():
          result.append(" ")
      result.append(ch)
  return "".join(result)

print(breakCamelCase("camelCasing"))
