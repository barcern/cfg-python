# This program uses random to simulate a coin flip.
# To finish the program you will need to add the following:
# - If the random coin flip matches the choice input by the user then they win
# - Otherwise if the random coin flip does not match the choice input by the user then they lose

# Import random
import random as r

def flip_coin():
    random_number = r.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side

choice = input('heads or tails: ')
result = flip_coin()
print('The coin landed on {}'.format(result))

# If loop to determine whether the user won
if (result == choice):
    print("Congratulations, you won!")
else:
    print("Better luck next time!")