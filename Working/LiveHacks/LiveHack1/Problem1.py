'''
-------------------------------------------------------------------------------
Name:		Problem1.py
Purpose:	Celsius to Fahrenheit Converter

Author:	Muzhao.G

Created:	02/10/2019
------------------------------------------------------------------------------
'''

# display title
print("""
-----------------------------------
| CELSIUS TO FAHRENHEIT CONVERTER |
-----------------------------------
""")

# display function of program
print("""
This program converts Celsius degrees temperature to Fahrenheit temperature
""")

# pause message
pause = input("Press enter to continue")

# define loop
while True:
    # obtain temperature in Celsius degrees from user input
    print(" ")
    celsius = float(input("Enter the Celsius degrees temperature: "))

    # define Fahrenheit in terms of Celsius
    fahrenheit = (9/5)*celsius + 32

    # display Fahrenheit temperature
    print("The Fahrenheit temperature is " + str(round(fahrenheit, 2)))

    # pause message
    pause2 = input("Press enter to input another Celsius degrees temperature")
