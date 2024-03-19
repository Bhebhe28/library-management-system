
# Task 2: Comprehensions

# List of codes for programming related books
programming_codes = [14, 15, 16, 17, 18, 19, 20]

# Normal list displaying the codes
print("Normal List of Programming Codes:")
print(programming_codes)

# Comprehensive list adding the codes together
sum_of_codes = sum([code for code in programming_codes])
print("\nSum of Programming Codes:", sum_of_codes)

# Comprehensive list displaying only odd codes
odd_programming_codes = [code for code in programming_codes if code % 2 != 0]
print("\nOdd Programming Codes:", odd_programming_codes)

# Comprehensive list displaying codes multiplied by 2
doubled_programming_codes = [code * 2 for code in programming_codes]
print("\nDoubled Programming Codes:", doubled_programming_codes)

# Set of programming codes
programming_codes_set = set(programming_codes)
print("\nSet of Programming Codes:", programming_codes_set)
