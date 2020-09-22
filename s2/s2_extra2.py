# Now extend the above so that it is a function, in which you
# have divisible_by, lower_bound, upper_bound as arguments.

def divisible_by_range(divisible_by, lower_bound, upper_bound):
    print('Checking for divisibility by {} in range {} - {}.'.format(divisible_by, lower_bound, upper_bound))
    for i in range(lower_bound, upper_bound):
        check = i % divisible_by
        if (check == 0):
            print(i)

divisible_by_range(3,237,259)