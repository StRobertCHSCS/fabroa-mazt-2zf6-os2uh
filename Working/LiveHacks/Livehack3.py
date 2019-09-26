# Question: Write a program that lets you enter a number of minutes, and that
# willl calculate the number of days, hours and minutes that it respresents

# User Interface Introduction: Title: Display: Minutes to Days Converter
print("""
-----------------------------
| MINUTES TO DAYS CONVERTER |
-----------------------------
""")

# User Interface Introduction: Function: Display: This program converts minutes
# into days, hours and minutes
print("This program converts minutes into days, hours and minutes.")

# Clear database of the wanted variables; reset minutes and hours
minutes = 0
hours = 0

# Let the user define the total amount of minutes
total_minutes = int(input("Enter the number of minutes you wish to calculate for: "))

# Define all variables (hours, days and minutes) with regards to the number of
# minutes
total_hours = total_minutes//60
remainder_minutes = total_minutes % 60
total_days = total_hours//24
remainder_hours = total_hours % 24

# Display the number of days, hours and minutes
print("""
This corresponds to:
""", total_days, "days,", remainder_hours, "hours, and", remainder_minutes, "minutes.")
