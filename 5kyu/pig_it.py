# Description:
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
  result = ""
  p_list = []
  n_list = []
  p_list = text.split()
  for word in p_list:
    word += word[0]
    word = word [1:]
    if word.isalpha():
      word+="ay"
    n_list.append(word)
  
  for word in n_list:
    result+=word
    result+=" "
  
  result = result[:-1:]
  
  return result

print(pig_it("O tempora o mores !"))