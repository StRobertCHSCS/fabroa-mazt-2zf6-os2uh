# Question: Write a program that lets you enter a degree measure in Fahrenheit
# , and that prints the result in celsius degree measure.

# Display: Fahrenheit to Celsius Converter
print("""
-----------------------------------
| FAHRENHEIT TO CELSIUS CONVERTER |
-----------------------------------
""")

# Display: This program will convert a Fahrenheit into Celsius degrees
print("""
This program will convert a Fahrenheit temperature into Celsius degrees
""")

# Convenient User Interface; a pause message
input("Press enter to continue")

# Let the user input the Fahrenheit temperature
print(" ")
fahrenheit_temperature = int(input("Enter your Fahrenheit temperature: "))

# Print out the Celsius temperature in terms of Fahrenheit temperature
print("""
The corresponding Celsius degrees is
""", (5/9)*(fahrenheit_temperature - 32))
