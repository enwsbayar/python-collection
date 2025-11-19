# Write a simple regex to validate a username. Allowed characters are:

# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

def validate_usr(username):
  s = str(username)
  if not 4 <= len(s) <= 16:
    return False
  for ch in s:
    if not ('a' <= ch <= 'z' or '0' <= ch <= '9' or ch == '_'):
      return False
  return True