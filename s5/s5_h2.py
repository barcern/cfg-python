# This program should save my data to a file, but it doesn't work when I run it. What is the problem
# and how do I fix it?

# Code provided
poem = 'I like Python and I am not very good at poems'

# Should open poem in write mode, not read mode
with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)
