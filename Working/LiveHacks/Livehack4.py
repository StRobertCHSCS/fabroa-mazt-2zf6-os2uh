temperature = float(input("Temperature"))
velocity = float(input("Windspeed"))

wind_chill_factor = float(13.12 + (0.612 * temperature) - (11.37 * (velocity ** 0.16)) + (0.3965 * temperature * (velocity ** 0.16)))
print("The wind chill factor is", wind_chill_facotr)