# Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450   -> 145
# 960000 -> 96
# 1050   -> 105
# -1050  -> -105
# 0      -> 0

# Note: Zero should be left as it is.

def no_boring_zeros(n):
  return 0 if not n else int((str(n)).rstrip("0"))

print(no_boring_zeros(960000))