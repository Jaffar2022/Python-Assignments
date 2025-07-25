#Task1

'''filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        print("Reading file content:")
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
'''

#Task2

filename = "output.txt"

# Step 1: Write user input to the file
text_to_write = input("Enter text to write to the file: ")
with open(filename, 'w') as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.\n")

# Step 2: Append more data to the file
text_to_append = input("Enter additional text to append: ")
with open(filename, 'a') as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.\n")

# Step 3: Read and display the final content
print(f"Final content of {filename}:")
with open(filename, 'r') as file:
    content = file.read()
    print(content)


