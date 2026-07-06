# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

# N! = 1 * 2 * 3 *  ... * N

# Be careful 1000! has 2568 digits...

# For more info, see: http://mathworld.wolfram.com/Factorial.html

# Examples
# N	Product	N factorial	Trailing zeros
# 6	1*2*3*4*5*6	720	1
# 12	1*2*3*4*5*6*7*8*9*10*11*12	479001600	2
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
def zeros(n: int) -> int:
	"""Return the number of trailing zeros in n!.

	Trailing zeros are created by factors 10 = 2*5. Since factors of 2
	are more common than 5, count the number of factors of 5 in n!.
	This is sum_{k>=1} floor(n / 5^k).
	"""
	count = 0
	power = 5
	while power <= n:
		count += n // power
		power *= 5
	return count


if __name__ == "__main__":
	# quick examples
	print(zeros(6))   # 1
	print(zeros(12))  # 2