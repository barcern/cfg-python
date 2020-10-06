# Using a for loop, output the values name, colour and price of each dictionary in the list

# Provided list
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]

# For loop to output requested values
for item in fruits:
    print(item['name'])
    print(item['colour'])
    print(item['price'])
    print("\n")
