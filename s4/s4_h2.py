# I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of
# different chocolates that I sell.
# I've started the program and included the chocolates and their prices. Finish the program by asking
# the user to input an item and then output its price.

# Provided list
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

# User input
chosen_item = input("Which item are you interested in? white/milk/dark/vegan ")

# Output price
if chosen_item in chocolates:
    cost = chocolates[chosen_item]
    print("The cost of {} chocolate is £{}.".format(chosen_item, cost))
else:
    print("Sorry, we do not stock this item.")
