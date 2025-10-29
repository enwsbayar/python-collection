# You are given two positive integers a and b (a < b <= 20000). Complete the function which returns a list of all those numbers in the interval [a, b) whose digits are made up of prime numbers (2, 3, 5, 7) but which are not primes themselves.

# Be careful about your timing!

# Good luck :)

def not_primes(a, b):
  primes_digits = {'2', '3', '5', '7'}
  res = []
  for n in range(a, b):
    s = str(n)
    if set(s).issubset(primes_digits):
      if n < 2:
        res.append(n)
        continue
      for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
          res.append(n)
          break
  return res