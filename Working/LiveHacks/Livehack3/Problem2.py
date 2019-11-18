'''
-------------------------------------------------------------------------------
Name:		Problem2.py
Purpose:	This program reads if the angles of the triangle match up to be an
            Equilateral, Isosceles or Scalene triangle.

Author:	Muzhao.G

Created:	18/11/2019
------------------------------------------------------------------------------
'''

# display introduction
print("Welcome to the Triangle Checker")

# get angles
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# check if it is a triangle
if angle1 + angle2 + angle3 == 180:
    # check if it is equilateral
    if angle1 and angle2 == 60:
        # display the triangle type
        print("A triangle with angles 60, 60, and 60 forms an Equilateral "\
        "triangle")

    else:
        # check if it is isosceles

        if (angle1 == angle2) or (angle2 == angle3) or (angle1 == angle3):

            # display the triangle type
            print("A triangle with angles " + str(angle1) + ", " + str(angle2)
            + ", and " + str(angle3) + " forms an Isosceles triangle.")

        else:
            # display the triangle type
            print("A triangle with angles " + str(angle1) + ", " + str(angle2)
            + ", and " + str(angle3) + " forms a Scalene triangle.")    
else:
    # display error message
    print("Error, the angles do not form a triangle.")
