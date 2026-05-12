# Wilson primes satisfy the following condition. Let 
# P
# P represent a prime number.
# Then,
# (
# P
# −
# 1
# )
# !
# +
# 1
# P
# ∗
# P
# P∗P
# (P−1)!+1
# ​
# should give a whole number, where 
# P
# !
# P! is the factorial of 
# P
# P.

# Your task is to create a function that returns true if the given number is a Wilson prime and false otherwise.

def am_i_wilson(p):
    factorial = 1
    for i in range(2, p):
        factorial *= i
    return (factorial + 1) % (p * p) == 0