# Whenever I’m shopping and I buy some bread I always forget to buy butter. Create a list and
# if 'bread' is in the list, add 'butter' to the shopping list.
# Try running the program with and without bread in the list to check that your program works.
# Remember the in operator checks if an item is in a list and the .append() method adds an item to a list.

# Create list
shopping = ['tomatoes', 'chickpeas', 'bread']

# Check if bread is in list and append butter if True
if 'bread' in shopping:
    shopping.append('butter')

print(shopping)
