# Question: Write a program that lets you enter a degree measure in Fahrenheeit
# , and that prints the result in celsius degree measure.

# User Interface Introduction
print("""
This program will convert a Fahrenheit temperature into Celsius degrees
""")

# Convenient User Interface
input("Press enter to continue")

# Defining the Fahrenheit temperature for which the user inputs
fahrenheit_temperature = int(input("Enter your Fahrenheit temperature: "))

# Defining Celsius in terms of Fahrenheit; prints out the corresponding Celsius
# temperature.
print("""
The corresponding Celsius degrees is
""", (5/9)*(fahrenheit_temperature - 32))
