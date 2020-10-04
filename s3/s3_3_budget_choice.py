# Rewrite the output of your burger program to use if statements
# If it is a good choice it should be:
# This restaurant is a great choice!
# If it is not a good choice it should be:
# Probably not a good idea

# Taking code from 3-2
# User input and set budget
price = float(input("How much does this burger cost? "))
veggie = input("Does this restaurant provide vegetarian options? y/n ")
budget = 10.0

# Check whether price is within the budget and veggie options are available
in_budget = price <= budget
veggie_friendly = veggie == 'y'
criteria = in_budget and veggie_friendly

# If loop to print feedback
if (criteria == True):
    print("This restaurant is a great choice!")
else:
    print("Probably not a good idea")
