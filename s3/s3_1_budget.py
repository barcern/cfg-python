# You have a budget of £10 and want to write a program to decide which burger restaurant to go to.
# - Input the price of a burger using input()
# - Check whether the price is less than or equal (<=) 10.00
# - Print the result in the format below
# Burger is within budget: True

# User input and set budget
price = float(input("How much does this burger cost? "))
budget = 10.0

# Check whether price is within the budget
in_budget = price <= budget

# Print result
print(f"Burger is within budget: {in_budget}")
#print("Burger is within budget: {}".format(in_budget))