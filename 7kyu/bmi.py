# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"

def bmi(weight, height):
  bmi = weight/pow(height, 2)
  return "Underweight" if bmi<=18.5 else "Normal" if bmi<=25.0 else "Overweight" if bmi <= 30.0 else "Obese"

print(bmi(50, 1.00))