# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

def prime_factors(n):
  res = []
  p = 2
  while p * p <= n:
    if n % p == 0:
      cnt = 0
      while n % p == 0:
        n //= p
        cnt += 1
      res.append(f"({p})" if cnt == 1 else f"({p}**{cnt})")
    p += 1 if p == 2 else 2
  if n > 1:
    res.append(f"({n})")
  return "".join(res)