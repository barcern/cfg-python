# Following on from previous exercise, use append instead of read and write.

# Ask for user input
item = input("What would you like to add to your to do list? ")

# Append to the existing file and print contents
file = 's5_2_todo.txt'
with open(file, 'a') as f:
    f.write(item)
