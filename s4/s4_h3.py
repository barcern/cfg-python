# Write a program that simulates a lottery. The program should have a list of seven numbers that
# represent a lottery ticket. It should then generate seven random numbers. After comparing the two
# sets of numbers, the program should output a prize based on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

import random as r

# Choose my numbers between 1 and 45
my_list = [3, 12, 38, 23, 32, 7, 11]

# Pick 7 random numbers between 1 and 45
winning_list = []
while len(winning_list) < 7:
    random_choice = r.randint(1, 45)
    if random_choice not in winning_list:
        winning_list.append(random_choice)
    else:
        pass

# Compare my choice to winning numbers
counter = 0
for i in my_list:
    if i in winning_list:
        counter += 1
    else:
        pass

# Provide winning information
if counter == 7:
    prize = 1000000
elif counter == 6:
    prize = 10000
elif counter == 5:
    prize = 100
elif counter == 4:
    prize = 40
else:
    prize = 0

print("Your choice: {}".format(my_list))
print("Winning set: {}".format(winning_list))
print(f"You have won £{prize} since {counter} of your numbers matched the winning set.")
