# Your task is to write an update for a lottery machine. Its current version produces a sequence of random letters and integers (passed as a string to the function). Your code must filter out all letters and return unique integers as a string, in their order of first appearance. If there are no integers in the string return "One more run!"

# Examples
# "hPrBKWDH8yc6Lt5NQZWQ"  -->  "865"
# "ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
# "555"                   -->  "5"

def lottery(s):
  return "".join(dict.fromkeys(c for c in s if c.isdigit())) if len([c for c in s if c.isdigit()]) > 0 else "One more run!"

print(lottery("hPrBKWDH8yc6Lt5NQZWQ"))