# Fix code below to ensure everything is printing properly.

# Settings chairs variable to be a variable, not a string
#chairs = '15''
chairs = 15
nails = 4
total_nails = chairs * nails

# Setting the print statement to print the message directly
message = 'I need to buy {} nails'.format(total_nails)
#print('You need to buy {} nails'.format(message))
print(message)