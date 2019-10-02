# Question: Write a program that lets you enter a number of minutes, and that
# willl calculate the number of days, hours and minutes that it respresents

# Display: Minutes to Days Converter
print("""
-----------------------------
| MINUTES TO DAYS CONVERTER |
-----------------------------
""")

# Display: This program converts minutes
# into days, hours and minutes
print("This program converts minutes into days, hours and minutes.")

# Define variables
minutes = 0
hours = 0

# Let the user define the total amount of minutes
total_minutes = \
    int(input("Enter the number of minutes you wish to calculate for: "))

# Define all variables (hours, days and minutes) in minutes
total_hours = total_minutes//60
actual_minutes = total_minutes % 60
days = total_hours//24
actual_hours = total_hours % 24

# Display the number of days, hours and minutes
print("""
This corresponds to:
""", days, "days,", actual_hours, "hours, and", actual_minutes, "minutes.")
