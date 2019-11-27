# 2_LiveHackPractice1.py

'''
A right-angled triangle has the property that when the values of the lengths 
of the sides are squared, the sum of the two smaller values is equal to the 
larger value. For example, 12, 5, and 13 make a right-angled triangle, because 
12 * 12 = 144, 5 * 5 = 25, 13 * 13 = 169, and 144 + 25 = 169.

Write a program that asks the user to enter three values and then determines 
whether the triangle created is a right-angled triangle or not.  Do not assume
that the sides are entered in order of smallest to greatest.  (i.e you don’t 
prompt them to enter the hypotenuse).


1. Create a flowchart of a solution to the problem.

2. Create the program in Pycharm
'''
import math

print(" ")
print("Insert three sides of a triangle and this program will explore all "\
"computable values of that triangle.")
print(" ")
numbers = []
equisides = 0

# get sides of triangle
while_condition = 1
while while_condition == 1:
    n = 0
    print("Enter the sides of the triangle")
    while n <= 2:
        numbers.append(float(input()))
        n += 1
    numbers.sort()

    if numbers[0] + numbers[1] <= numbers[2]:
        print("Invalid triangle side values")
        numbers = []
    else:
        while_condition = 0

# computing angle type of triangle
if numbers[0] == numbers[1] or numbers[1] == numbers[2]:
    if numbers[0] == numbers[2]:
        equisides = 3
    else:
        equisides = 2
else:
    equisides = 1

# critical angle
two_legs_angle_radians = math.acos((numbers[0]**2 + numbers[1]**2 - 
numbers[2]**2)/(2*numbers[0]*numbers[1]))

two_legs_angle_degrees = math.degrees(two_legs_angle_radians)

# other angles
smallest_largest_angle_radians = math.acos((numbers[0]**2 + numbers[2]**2 -
numbers[1]**2)/(2*numbers[0]*numbers[2]))

middle_largest_angle_radians = math.acos((numbers[1]**2 + numbers[2]**2 -
numbers[0]**2)/(2*numbers[1]*numbers[2]))

# sides equilateral, isosceles or scalene?
if equisides == 3:
    equisides_value = str("equilateral")
if equisides == 2:
    equisides_value = str("isosceles")
if equisides == 1:
    equisides_value = str("scalene")

# angles right, acute or obtuse?
if round(two_legs_angle_degrees, 3) <= 90:
    angle_value = str("acute")
if round(two_legs_angle_degrees, 3) >= 90:
    angle_value = str("obtuse")
if round(two_legs_angle_degrees, 3) == 90:
    angle_value = str("right")

# get preferred angle style
while_condition2 = 0
while while_condition2 == 0:
    print("Press 1 for angle values in degrees. Press 2 for"\
    " values in radians.")
    angle_style = int(input(""))
    if angle_style != 1 and angle_style != 2:
        print("Invalid value")
    else:
        while_condition2 = 1

# calculate perimeter
perimeter = numbers[0] + numbers[1] + numbers[2]

# calculate area
semiperimeter = perimeter/2
area = math.sqrt(semiperimeter*(semiperimeter - numbers[0])*(semiperimeter -
numbers[1])*(semiperimeter - numbers[2]))

# print all values of triangle
print(" ")
print("------------------------------------------------")
print("This triangle is a " + angle_value + " " + equisides_value + " triangle.")
print("Triangle sides:")
print(str(round(numbers[0], 3)))
print(str(round(numbers[1], 3)))
print(str(round(numbers[2], 3)))
print(" ")

print("Triangle angles:")
if angle_style == 1:
    # angles in degrees
    print(str(round(two_legs_angle_degrees, 3)))
    print(str(round(math.degrees(smallest_largest_angle_radians),3)))
    print(str(round(math.degrees(middle_largest_angle_radians), 3)))
elif angle_style == 2:
    # angles in radians
    print(str(round(two_legs_angle_radians, 3)))
    print(str(round(smallest_largest_angle_radians, 3)))
    print(str(round(middle_largest_angle_radians, 3)))
else:
    print("Error. Please restart program")

print(" ")
print("Perimeter:")
print(str(round(perimeter, 3)))
print("Area:")
print(str(round(area, 3)))
print("------------------------------------------------")