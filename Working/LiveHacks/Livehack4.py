# Question: Write a program that gets the temperature (Celsius) and windspeed
# (km/h) then computes and outputs the windchill factor

# Display: Windspeed Calculator
print("""
-------------------------
| WINDSPEED  CALCULATOR |
-------------------------
""")

# Display: This program will output a windchill factor based on the given
# temperature and velocity this user wishes to calculate with
print("""
This program will output a windchill factor based on the given temperature and
velocity this user wishes to calculate with.
""")

input("Press enter to continue")

# Obtain temperature from user input
print(" ")
temperature = float(input("Choose the temperature you wish to input: "))

# Obtain wind speed from user input
velocity = float(input("Choose the windspeed you wish to input: "))

# Display the wind chill factor based on the temperature and wind speed
wind_chill_factor = 13.12 + (0.612 * temperature) - \
    (11.37 * (velocity ** 0.16)) + (0.3965 * temperature * (velocity ** 0.16))
print("The wind chill factor is", round(wind_chill_factor, 2))
