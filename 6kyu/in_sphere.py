# You will be given an array of coordinates and a radius. The function should return whether the point described by these coordinates lies within the given radius from the origin.

# - In two dimensions, a point [x, y] lies within a circle of radius r if:

#   x^2 + y^2 <= r^2

# - In higher dimensions, this generalizes to:

#   x^2 + y^2 + z^2 + ... <= r^2

# Note: A point with no coordinates should return true, because in zero dimensions all points coincide at the origin.

def in_sphere(coords, radius):
  return sum([i**2 for i in coords]) <= radius**2

print(in_sphere([3, 4, 5], 6))