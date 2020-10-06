# Write a Python program to count the number of strings where the string length is 2
# e.e for the list words = ['hi', 'hello', 'no', 'is'] should give an output of 3

# Create a list and initialise a counter
string_list = ['hello', 'hi', 'am', 'table', 'egg', 'ok']
counter = 0

# Loop over all values in string_list
for item in string_list:
    # Check whether item is 2 characters long
    if len(item) == 2:
        # Increase the counter
        counter += 1
    else:
        pass

# Print the answer
print(f"There are {counter} 2-character string in the provided list.")