# Question: Write a program that lets you enter a number of minutes, and that
# willl calculate the number of days, hours and minutes that it respresents

# User Interface Introduction: Title
print("""
-----------------------------
| MINUTES TO DAYS CONVERTER |
-----------------------------
""")

# User Interface Introduction: Function
print("This program converts minutes into days, hours and minutes.")

# Clearing database of the wanted variables
minutes = 0
hours = 0

# Defining the total amount of minutes
total_minutes = int(input("Enter the number of minutes you wish to calculate for: "))

# Defining all variable (hours, days and minutes) with regard to the number of
# minutes
total_hours = total_minutes//60
remainder_minutes = total_minutes % 60
total_days = total_hours//24
remainder_hours = total_hours % 24

# Displaying the number of days, hours and minutes
print("""
This corresponds to:
""", total_days, "days,", remainder_hours, "hours, and", remainder_minutes, "minutes.")
