# Now that you've finished your burger, you want to pay for your food.
# Let's write a program to calculate your meal and apply a discount if
# applicable.
# If your total meal costs more than £20 and you have a discount, the
# price will be reduced by 10%. The program should print "Discount applied"
# or "No discount" depending on whether the discount criteria was met.

# User input
meal_price = float(input("How much did your meal cost? "))
discount_available = input("Do you have a discount code? y/n ")

# Verify whether discount is applicable
discount_applicable = (meal_price > 20) and (discount_available == 'y')

# Print relevant response
if (discount_applicable):
    meal_price = meal_price * 0.9
    print("Discount applied. Total cost is £{}.".format(meal_price))
else:
    print("No discount. Total cost is £{}.".format(meal_price))