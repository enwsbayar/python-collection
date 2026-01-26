# Combine strings function
# Create a function named combineNames/combine_names/CombineNames that accepts two parameters (first and last name). The function should return the full name.

# Example:

# With "James" as the first name and "Stevens" as the last name should return "James Stevens"
def combine_names(first_name, last_name):
  fn = '' if first_name is None else str(first_name).strip()
  ln = '' if last_name is None else str(last_name).strip()
  return (fn + ' ' + ln).strip()