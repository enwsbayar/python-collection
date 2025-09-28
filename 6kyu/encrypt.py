# Description:
# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

def encrypt_this(text):
  if not text:
    return ""
  
  words = text.split()
  encrypted_words = []

  for word in words:
    if len(word) == 1:
      encrypted_words.append(str(ord(word[0])))
    elif len(word) == 2:
      encrypted_words.append(str(ord(word[0])) + word[1])
    else:
      first = str(ord(word[0]))
      middle = word[2:-1]
      second_last = word[-1]
      second = word[1]
      encrypted_words.append(first + second_last + middle + second)
    
  return ' '.join(encrypted_words)


print(encrypt_this("Hello dwqd wqd qw"))


