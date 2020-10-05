# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

# Get user input
is_raining = input("Is it raining outside? y/n ")

# Conditional loop
if (is_raining == 'y'):
    print("Take an umbrella")
elif (is_raining == 'n'):
    print("You don't need an umbrella")
else:
    print("Please provide a valid input")