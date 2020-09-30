# Ask the user to enter the following three things using input():
# The amount they want to bet
# A colour (red or black)
# A number between 1 and 100
# After generating a random number and colour:
# If the colour matches, the users keeps the amount that was bet
# If the number matches, the users wins double the amount that was bet
# If the colour and number matches, the users wins 100 times the amount that was bet
# When neither the colour or number matches the user wins 0
# Output the amount the user won

# Import random module
import random as r

# User input
bet = float(input("How much would you like to bet? "))
colour = input("Choose: red or black? ")
number = int(input("Choose number between 1 and 100: "))

# Generate random number and colour
random_number = r.randint(1, 100)

def choose_random_colour():
    value = r.randint(1, 2)
    if (value == 1):
        return 'red'
    else:
        return 'black'

random_colour = choose_random_colour()

# Game rules
if (colour == random_colour):
    win = bet
    print("User keeps the amount that was bet")
elif (number == random_number):
    win = bet * 2
elif (colour == random_colour) and (number == random_number):
    win = bet * 100
else:
    win = 0

# Output amount won
print(f"You have just won {win}, congratulations!")