# Given a text file “input.txt” that contains a paragraph, count the number of words in the file.
# The output should look as below:
#         Number of words in file are xxxxx
# Hint: Use the split() method on a string to split the string into a list. The default separator is a whitespace.

# Read file
file = 's5_extra1_input.txt'
with open (file, 'r') as f:
    contents = f.read()

print(contents)

# Using split()
separated = contents.split(" ")
words = len(separated)

# Print message
print(f"Number of words in file is {words}")
