# Write a program to create a random name. You should have a list of random first-names
# and a list of last-names. Choose a random item from each and display the result.
# Extension: Using list of verbs and a list of nouns, create randomised sentences

import random

# Create lists
first_list = ['emma', 'tom', 'josh', 'duncan', 'jack']
last_list = ['smith', 'bloggs', 'jones', 'williams', 'davies']
verb_list = ['likes', 'hates', 'doesn\'t mind', 'is afraid of']
noun_list = ['planes', 'cats', 'spiders', 'mugs']

# Generate random names
first = random.choice(first_list).title()
last = random.choice(last_list).title()
verb = random.choice(verb_list)
noun = random.choice(noun_list)

# Print the name
print(first, last, verb, noun)
