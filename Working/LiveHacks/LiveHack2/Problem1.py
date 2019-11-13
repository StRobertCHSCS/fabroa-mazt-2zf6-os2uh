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

print("<info_on_program>")
numbers = []
equisides = 0

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
    else:
        while_condition = 0

if numbers[0] == numbers[1] or numbers[1] == numbers[2]:
    if numbers[0] == numbers[2]:
        equisides = 3
    else:
        equisides = 2
else:
    equisides = 1

two_legs_angle_radians = math.acos((numbers[0]**2 + numbers[1]**2 - 
numbers[2]**2)/(2*numbers[0]*numbers[1]))

two_legs_angle_degrees = math.degrees(two_legs_angle_radians)

smallest_largest_angle_radians = math.acos((numbers[0]**2 + numbers[2]**2 -
numbers[1]**2)/(2*numbers[0]*numbers[2]))

middle_largest_angle_radians = math.acos((numbers[1]**2 + numbers[2]**2 -
numbers[0]**2)/(2*numbers[1]*numbers[2]))

if equisides = 3:
    equisides_value = str("equilateral")
if equisides = 2:
    equisides_value = str("isosceles")
if equisides = 1:
    equisides_value = str("scalene")

if round(two_legs_angle_degrees, 3) == 90:
    angle_value = str("right")
if round(two_legs_angle_degrees, 3) <= 90:
    angle_value = str("acute")
if round(two_legs_angle_degrees, 3) >= 90:
    angle_value = str("obtuse")

angle_style = int(input("Would you prefer your angle values in"))
print("sides =", str(equisides), ", angle =", 
str(round(two_legs_angle_degrees, 5)))
