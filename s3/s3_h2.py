# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've
# written a program to check that I can afford the cost, but something doesn't seem right.
# Fix the mistake.

# Mistake 1: boat cost should be called boat_cost
# Mistake 2: my_money should be converted to float
# Mistake 3: missing indentation in if-else loop
# Mistake 4: comparison operator the wrong way round
# Mistake 5: comparison operator should be >= not >
# Mistake 6 - doesn't look neat: unnecessary blank space in else :
my_money = float(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money >= boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')
