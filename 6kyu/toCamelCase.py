# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def toCamelCase(text):
  wordsT = []
  flat = []
  result = ""
  if not text.count("-"):
    words = text.split("_")
  if not text.count("_"):
    words = text.split("-")
  else:
    wordsTemp = text.split("-")
    for word in wordsTemp:
      words = word.split("_")
      wordsT.append(words)
      flat = [item for sublist in wordsT for item in sublist]
  
  if flat:
    words = flat

  for word in words:
    if word != words[0]:
      word = word.capitalize()
      result += word
    else:
      result += word
  
  return result


print(toCamelCase("the_stealth-warrior"))