# Make a list of game scores. Using list functions write code to output information of the scores
# in the following format:
# Number of scores: 10
# Highest score: 200
# Lowest score: 3
# Extension: Output all of the scores in descending order

# Create a list of scores
scores = [4, 12, 16, 33, 295, 1, 55, 3]

# Print specified information
print("Number of scores: ", len(scores))
print("Highest score: ", max(scores))
print("Lowest score: ", min(scores))

# Print scores in descending order
# Must use list() since reversed() returns an iterator
print(list(reversed(sorted(scores))))
