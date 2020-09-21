# Calculate how many omelettes we can make with a given number of boxes of eggs.
# Presume that a box of eggs contains 6 eggs and we need 4 eggs per omelette.

# Calculate how many omelettes we can make
box_eggs = 6
eggs_per_box = 6
total_eggs = box_eggs * eggs_per_box
eggs_per_omelette = 4
omelettes = total_eggs / eggs_per_omelette

# Print message
message = "We can make {} omelettes with {} boxes of eggs.".format(omelettes, box_eggs)
print(message)