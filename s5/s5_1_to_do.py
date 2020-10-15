# Create a to-do list program that writes user input to a file.
# The program should:
# - Ask the user to input a new to-do item
# - Read the contents of the existing to-do items
# - Add the new to do item to the existing to-do items
# - Save the updated to-do items
# You will need to manually create a new file called todo.txt.

# Ask for user input
item = input("What would you like to add to your to do list? ")

# Read the existing file and print contents
file = 's5_1_todo.txt'
with open(file, 'r') as f:
    contents = f.read()
print(contents)

# Add new item to file
with open(file, 'w') as f:
    new_contents = contents + '\n' + item
    f.write(new_contents)
