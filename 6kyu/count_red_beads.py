# Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement below work out the number of red beads.

# @ @@ @ @@ @ @@ @ @@ @ @@ @

# Implement a function returning the number of red beads.
# If there are less than 2 blue beads return 0.


def count_red_beads(n):
  return 2 * (n - 1) if n >= 2 else 0
