# I want to work out how much money I've spent on lunch this week. I've created a list of what I spent each day.
# Write a program that uses a for loop to calculate the total cost

# List costs and initialise total_cost
costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

# For loop to sum up the costs
for item in costs:
    total_cost += item

# Print the total cost
print(f"The total cost of my lunches is £{total_cost:.2f}")

# Alternatively use sum() function
print(sum(costs))
