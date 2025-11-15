# 7 kyu: Digital Root
# Bir sayının dijital kökünü bulun: basamakları toplayın, sonuç tek basamaklı değilse tekrarlayın.
# Örnek:
# digital_root(16) -> 7  (1+6=7)
# digital_root(942) -> 6 (9+4+2=15 -> 1+5=6)
# digital_root(132189) -> 6

def digital_root(n):
  n = abs(int(n))
  while n >= 10:
    n = sum(int(d) for d in str(n))
  return n
