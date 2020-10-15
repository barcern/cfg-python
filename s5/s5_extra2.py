# Given two to do text files (todo1.txt and todo2.txt) containing a list of your to dos,
# combine them and write them out to a single file called “todo_combined.txt”

# Load first file
file1 = 's5_1_todo.txt'
with open(file1, 'r') as f:
    contents1 = f.read()

# Load second file
file2 = 's5_2_todo.txt'
with open(file2, 'r') as f:
    contents2 = f.read()

# Combine and save into third file
file3 = 's5_extra2_todo_combined.txt'
with open(file3, 'w+') as f:
    combined = "file1\n" + contents1 + "\nfile2\n" + contents2
    f.write(combined)
