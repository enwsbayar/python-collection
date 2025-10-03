# Write a function that removes every lone 9 that is inbetween 7s.

# "79712312" --> "7712312"
# "79797"    --> "777"

def seven_ate9(str_):
  result = []
  for i, ch in enumerate(str_):
    if ch == "9" and i > 0 and i < len(str_) - 1 and str_[i-1] == "7" and str_[i+1] == "7":
      continue
    result.append(ch)
  return "".join(result)

print(seven_ate9("79712312"))