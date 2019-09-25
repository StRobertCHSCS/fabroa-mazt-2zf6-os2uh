# Queston: Write a program that lets you enter a number of hours, and that
# converts it to days and hours.

# User Interface Introduction
print("""
---------------------------
| HOURS TO DAYS CONVERTER |
---------------------------
""")

# User Interface
print("This program will convert a given number of hours you wish to")
print("calculate into days and hours.")
input("Press enter to continue")

# Defining number of hours
hours = int(input("Enter the amount of hours you wish to calculate: "))

# Defining and displaying the number of days in terms of hours
print("That is equiavlent to", hours//24, "days and", hours % 24, "hours.")
