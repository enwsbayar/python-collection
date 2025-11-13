# Problem:
# Verilen bir tamsayı listesi için sadece pozitif sayıların toplamını döndüren bir fonksiyon yazın. Boş liste veya pozitif yoksa 0 döndürsün.

def sum_positive(arr):
  return sum(x for x in arr if x > 0)
