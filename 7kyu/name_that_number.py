# In this kata, you'll be given an integer of range 0 <= x <= 99 and have to return that number spelt out in English. A few examples:

# name_that_number(4)   # returns "four"
# name_that_number(19)  # returns "nineteen"
# name_that_number(99)  # returns "ninety nine"
# Words should be separated by only spaces and not hyphens. No need to validate parameters, they will always be in the range [0, 99]. Make sure that the returned String has no leading of trailing spaces. Good luck!

def name_that_number(n):
  ones = ["zero","one","two","three","four","five","six","seven","eight","nine"]
  teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen",
            "sixteen","seventeen","eighteen","nineteen"]
  tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

  if n < 10:
    return ones[n]
  elif n < 20:
    return teens[n-10]
  else:
    return tens[n//10] + (" " + ones[n%10] if n%10 != 0 else "")

print(name_that_number(23))