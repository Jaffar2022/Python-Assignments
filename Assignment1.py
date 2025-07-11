# Task 1 Program to perform basic mathematical operations on two numbers
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Displaying results
print("\nAddition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
'''


#Tas 2 Personalized Greeting

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate first and last name to form full name
full_name = first_name + " " + last_name

print("\nHello, " + full_name + "! Welcome to the Python program.")

