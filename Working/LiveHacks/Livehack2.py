# Queston: Write a program that lets you enter a number of hours, and that
# converts it to days and hours.

# Display: Hours to days converter
print("""
---------------------------
| HOURS TO DAYS CONVERTER |
---------------------------
""")

# Display: This program will convert a given number of hours you wish to
# calculate into days and hours
print("This program will convert a given number of hours you wish to")
print("calculate into days and hours.")

input("Press enter to continue")

# Let the user input the amount of hours
hours = int(input("Enter the amount of hours you wish to calculate: "))

# Display the number of days in terms of hours
print("That is equiavlent to", hours//24, "days and", hours % 24, "hours.")
