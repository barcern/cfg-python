# Add code to your burger program to input whether the restaurant has a vegetarian option
# The output should say whether the cost is within budget AND has a vegetarian option
# Restaurant meets criteria: True

# Taking code from 3-1
# User input and set budget
price = float(input("How much does this burger cost? "))
veggie = input("Does this restaurant provide vegetarian options? y/n ")
budget = 10.0

# Check whether price is within the budget and veggie options are available
in_budget = price <= budget
veggie_friendly = veggie == 'y'
criteria = in_budget and veggie_friendly

# Print result
print(f"Restaurant meets criteria: {criteria}")