'''
-------------------------------------------------------------------------------
Name:		Problem1.py
Purpose:	The school has decided to offer cash bonuses to homerooms that show
            an improvement in class average from mid-term to final. This program
            outputs the cash bonus that a homeroom will receive.

Author:	Muzhao.G

Created:	18/11/2019
------------------------------------------------------------------------------
'''

# get averages from input
midterm_average = float(input("Enter the mid-term average: "))
final_average = float(input("Enter the final average: "))

# calculate difference
difference = final_average - midterm_average

# check for value of difference
if difference >= 0.01:
    if difference <= 0.05:
        # display cash bonus
        print("Congratulations, the cash bonus is $100.")
    else:
        if difference <= 0.1:
            # display cash bonus
            print("Congratulations, the cash bonus is $300.")
        else:
            # display cash bonus
            print("Congratulations, the cash bonus is $600.")
else:
    # display no cash bonus
    print("Sorry, no cash bonus for your class.")