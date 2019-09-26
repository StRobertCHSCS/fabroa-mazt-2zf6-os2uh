# Question: Write a program that gets the temperature (Celsius) and windspeed
# (km/h) then computes and outputs the windchill factor

# User Interface Introduction: Display: Windspeed Calculator
print("""
-------------------------
| WINDSPEED  CALCULATOR |
-------------------------
""")

# User Interface: Display: This program will output a windchill factor based on
# the given temperature and velocity this user wishes to calculate with
print("""
This program will output a windchill factor based on the given temperature and
velocity this user wishes to calculate with
""")

# User Interface; convenient pause message
input("Press enter to continue")

# Let the user define the temperature that gets inputted
print(" ")
temperature = float(input("Choose the temperature you wish to input: "))

# Let the user define the windspeed that gets inputted
velocity = float(input("Choose the windspeed you wish to input windspeed: "))

# Display the wind chill factor based on the temperature and windspeed
wind_chill_factor = float(13.12 + (0.612 * temperature) - (11.37 * (velocity ** 0.16)) + (0.3965 * temperature * (velocity ** 0.16)))
print("The wind chill factor is", round(wind_chill_factor, 2))
