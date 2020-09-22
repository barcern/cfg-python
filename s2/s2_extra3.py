# Write a function called number_sum that takes a positive integer n as input and returns the sum of all the numbers
# between 1 and that number.

def number_sum(integer):
    sum = 0
    for i in range(integer + 1):
        sum = sum + i
    return sum

print(number_sum(10))