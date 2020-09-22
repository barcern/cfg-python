# Write a Python program to find the numbers which are divisible by 7,
# between 1500 and 2700 (both included). Each time you find a number,
# print it out.

for i in range(1500,2701):
    check = i % 7
    if (check == 0):
        print(i)
