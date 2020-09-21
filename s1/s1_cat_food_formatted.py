# Rewrite s1_cat_food.py to use string formatting.

cats = 10
cans_per_day = 2.5
days = 7

total_cans_per_day = cats * cans_per_day
total_cans_per_time = total_cans_per_day * days

# Using .format() method
line1 = "To feed 10 cats, we need {} cans each day.".format(total_cans_per_day)
line2 = "To feed 10 cats for {} days, we need {} cans in total.".format(days, total_cans_per_time)
print(line1)
print(line2)

# Using f-strings
line3 = f"To feed 10 cats, we need {total_cans_per_day} cans each day."
line4 = f"To feed 10 cats for {days} days, we need {total_cans_per_time} cans in total."
print(line3)
print(line4)