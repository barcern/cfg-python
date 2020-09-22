# You have friends at your house for dinner and you've accidentally
# burnt the lasagne. Time to order pizza.
# Write a program to calculate how many pizzas you need to feed you and your friends.

import math as m

friends_number = int(input('How many friends do you need to feed? '))
pizza_proportion = float(input('How many pizzas per friend do you need? '))

total_pizzas = friends_number * pizza_proportion
order_pizzas = m.ceil(total_pizzas)

message = 'Your friends are going to eat {} pizzas, so you should order {} pizzas.'.format(total_pizzas, order_pizzas)
print(message)