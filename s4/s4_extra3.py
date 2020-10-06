# Try to do the following on the provided dictionary:
# a. Add a key to inventory called ‘pocket’.
# b. Set the value of ‘pocket’ to be a list consisting of the strings ‘seashell’, ‘strange berry’, and ‘lint’
# c. Add 50 to the number stored under the ‘gold’ key.

# Provided dictionary
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'],
  'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Add a key called 'pocket'
inventory['pocket'] = None
print(inventory)

# Set value of 'pocket' key
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Add 50 to 'gold' key
inventory['gold'] = [500, 50]
print(inventory)