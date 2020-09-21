# Create a program that calculates how many cans of cat food you need to feed 10 cats, given a cat requires 2.5 cans of food a day
# Your will need:
# A variable for the number of cats
# A variable for the number of cans each cat eats in a day
# A print() function to output the result
# Extension: change the calculation to work out the amount needed for 7 days

cats = 10
cans_per_day = 2.5
days = 7

total_cans_per_day = cats * cans_per_day
total_cans_per_time = total_cans_per_day * days

print("To feed 10 cats, we need " + str(total_cans_per_day) + " cans each day.")
print("To feed 10 cats for " + str(days) + " days, we need " + str(total_cans_per_time) + " cans in total.")
