# This program is supposed to read data about trees from a file to find the shortest tree.
# Complete the program adding code to open trees.csv.
# The trees.csv file included with your student guides.
# Save the csv file in the same folder as your Python program.

import csv

# Complete the code to open the csv file and read the contents
file = 's5_3_csv_trees.csv'

with open(file, 'r') as csv_f:
    spreadsheet = csv.DictReader(csv_f)
    # Carry out tasks whilst file is open
    heights = []
    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)
print(heights)
