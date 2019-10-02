# 1_3_2_userinput.py
# This program will print the area and width of a given length and width
# that the user wishes to input.

print("This program will give you the area and width of a given length and")
print("width.")

input("Press enter to continue")

length = int(input("Enter the length you wish to calculate for: "))
width = int(input("Enter the width you wish to calculate for: "))

print("Area:", length*width)
print("Perimeter:", 2*(length + width))
