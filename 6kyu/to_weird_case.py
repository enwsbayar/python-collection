# Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

# Examples:
# "String" => "StRiNg"
# "Weird string case" => "WeIrD StRiNg CaSe"

def to_weird_case(words):
  words_list = words.lower().split(" ")
  new_words_list = []

  for w in words_list:
    new_word = ''
    for c in range(len(w)):
      if c % 2 == 0:
        new_word += w[c].upper()
      else:
        new_word += w[c]
    new_words_list.append(new_word)

  return " ".join(new_words_list)

print(to_weird_case("Weird string case"))
