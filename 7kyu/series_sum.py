# Task

# Write a function that returns the n-th term of the following series, which is the sum of the first n terms of the sequence.

# Series:
# 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + …

# You need to figure out the rule of the series to complete this.

# Rules:

# Round the answer to 2 decimal places and return it as a string.

# If the given value is 0, return "0.00".

# You will only be given natural numbers as arguments.

# Examples:

# n = 1 → 1 → "1.00"

# n = 2 → 1 + 1/4 → "1.25"

# n = 5 → 1 + 1/4 + 1/7 + 1/10 + 1/13 → "1.57"

def series_sum(n):
    return f"{sum(1/(3*i + 1) for i in range(n)):.2f}"

print(series_sum(3))