#Task1
'''
# Step 1: Create a dictionary with student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or an error message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
'''
#Task2

# Step 1: Create a list of numbers from 1 to 10
original_list = list(range(1, 11))

# Step 2: Extract the first five elements
extracted_elements = original_list[:5]

# Step 3: Reverse the extracted elements
reversed_elements = extracted_elements[::-1]

# Step 4: Print the results
print("Original list:", original_list)
print("Extracted first five elements:", extracted_elements)
print("Reversed extracted elements:", reversed_elements)
