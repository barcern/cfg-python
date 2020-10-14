# I have a list of things I need to buy from my supermarket of choice.
# I want to know what the first thing I need to buy is. However, when I run the program it shows me a
# different answer to what I was expecting?
# What is the mistake? How do I fix it?

shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board",
]

# List index starts at 0, not at 1
print(shopping_list[0])
