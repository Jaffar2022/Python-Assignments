#Task1: Calculate factorial using a function
'''
def factorial(n):
    if n < 2:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Taking input from the user
num = int(input("Enter a number: "))

# Calculating factorial
fact = factorial(num)

# Displaying the result
print(f"\nFactorial of {num} is: {fact}")

'''

#Tas2: Using Math Module for calculations

import math

# Ask user for input
num = float(input("Enter a number: "))

# Perform calculations
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

# Display results
print(f"\nSquare root: {sqrt_val}")
print(f"Logarithm: {log_val}")
print(f"Sine: {sine_val}")
