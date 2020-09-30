# You're cooking a pizza and need to check that the oven is at the right temperature.
# Write a program to:
# Ask the user to input the temperature
# Prints "The oven is too hot" if the temperature is over 200
# Prints "The oven is too cold" if the temperature is under 150
# Prints "The oven is at the perfect temperature" if the temperature is 180
# Prints "The temperature is close enough" for any other temperature

# User input
temperature = float(input("What is the temperature of the oven? "))

# If loops to check temperature
if (temperature > 200):
    print("The oven is too hot")
elif (temperature == 180):
    print("The oven is at the perfect temperature")
elif (temperature < 150):
    print("The oven is too cold")
else:
    print("The temperature is close enough")