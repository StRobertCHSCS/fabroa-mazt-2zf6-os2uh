# Queston: Write a program that lets you enter a number of hours, and that
# converts it to days and hours.

# User Interface Introduction: Display: Hours to days converter
print("""
---------------------------
| HOURS TO DAYS CONVERTER |
---------------------------
""")

# User Interface: Display: This program will convert a given number of hours
# you wish to calculate into days and hours
print("This program will convert a given number of hours you wish to")
print("calculate into days and hours.")

# User Interface; convenient pause message
input("Press enter to continue")

# Let the user input the amount of hours
hours = int(input("Enter the amount of hours you wish to calculate: "))

# Define and display the number of days in terms of hours
print("That is equiavlent to", hours//24, "days and", hours % 24, "hours.")
