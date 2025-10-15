# Write a method that takes a number and returns a string of that number in English.

# Your method should be able to handle any number between 0 and 99999. If the given number is outside of that range or not an integer, the method should return an empty string.

# Examples
# 0      -->  "zero"
# 27     -->  "twenty seven"
# 100    -->  "one hundred"
# 7012   -->  "seven thousand twelve"
# 99205  -->  "ninety nine thousand two hundred five"

def number_to_english(n):
  if not isinstance(n, int) or n < 0 or n > 99999:
    return ""

  ones = [
      "zero", "one", "two", "three", "four",
      "five", "six", "seven", "eight", "nine",
      "ten", "eleven", "twelve", "thirteen", "fourteen",
      "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
  ]

  tens = [
      "", "", "twenty", "thirty", "forty",
      "fifty", "sixty", "seventy", "eighty", "ninety"
  ]

  def two_digit(num):
    if num < 20:
      return ones[num]
    elif num % 10 == 0:
      return tens[num // 10]
    else:
      return tens[num // 10] + " " + ones[num % 10]

  def three_digit(num):
    if num < 100:
      return two_digit(num)
    elif num % 100 == 0:
      return ones[num // 100] + " hundred"
    else:
      return ones[num // 100] + " hundred " + two_digit(num % 100)

  if n < 100:
    return two_digit(n)
  elif n < 1000:
    return three_digit(n)
  elif n < 100000:
    thousands = n // 1000
    remainder = n % 1000
    if remainder == 0:
      return three_digit(thousands) + " thousand"
    else:
      return three_digit(thousands) + " thousand " + three_digit(remainder)
