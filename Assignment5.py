'''
#Task1 : Create dictionary with student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
'''
#Task2 : Demonstrate List Slicing

original_list = list(range(1, 11))

extracted_elements = original_list[:5]

reversed_elements = extracted_elements[::-1]

print("Original list:", original_list)
print("Extracted first five elements:", extracted_elements)
print("Reversed extracted elements:", reversed_elements)
