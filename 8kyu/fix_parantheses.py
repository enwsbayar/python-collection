# Your job is to fix the parentheses so that all opening and closing parentheses (brackets) have matching counterparts. You will do this by appending parenthesis to the beginning or end of the string. The result should be of minimum length. Don't add unnecessary parenthesis.

# The input will be a string of varying length, only containing '(' and/or ')'.

# For example:

# Input: ")("
# Output: "()()"

# Input: "))))(()("
# Output: "(((())))(()())"

def fix_parentheses(s):
  if not s:
      return s
  unmatched_closing = 0
  unmatched_opening = 0
  balance = 0
  for char in s:
      if char == '(':
          balance += 1
      elif char == ')':
          if balance > 0:
              balance -= 1
          else:
              unmatched_closing += 1
  unmatched_opening = balance
  result = '(' * unmatched_closing + s + ')' * unmatched_opening
  return result

print(fix_parentheses('())))(()))'))