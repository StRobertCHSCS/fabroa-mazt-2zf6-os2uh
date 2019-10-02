'''
-------------------------------------------------------------------------------
Name:		Problem2.py
Purpose:	Popeyes Chicken Distribution
Author:	Muzhao.G

Created:	02/10/2019
------------------------------------------------------------------------------
'''

# define loop variable
identifier = 0

# display title
print("""
------------------------------------
| MR. FABROA's CHICKEN DISTRIBUTER |
------------------------------------
""")

# display function
print("""
Students in Mr. Fabroa's class have won a contest and will receive pieces of
Popeyes Chicken to be distributed among each other evenly.
The remaining pieces will be set aside for Mr. Fabroa.
As Mr. Fabroa, you get to choose hamong each other evenly.
The remaining pieces will be set aside for Mr. Fabroa.
As Mr. Fabroa, you get to choose how many chickens you want each person to get.
""")

# obtain variables from user
number_of_students = int(input("How many students are there in the class? "))
number_of_chickens = int(input("How many pieces of chicken are there to " +
                               "distribute? "))

# define Loop
while True:
    # obtain number of chickens each student gets from user input
    # define maximum amount of chickens each student gets
    student_chickens = int(input("How many pieces of chicken does each " +
                                 "student get? Maximum is " +
                                 str(number_of_chickens//number_of_students) + 
                                 ": "))

    # check to see if the number of chickens each student receives is greater
    # than the maximum amount of chickens each student gets
    if student_chickens <= number_of_chickens//number_of_students:

        # display number of chickens for each student
        print("Each student gets " + str(student_chickens) + " chickens.")

        # display number of chickens for Mr. Fabroa
        print("Mr. Fabroa gets " + 
              str(number_of_chickens - number_of_students*student_chickens) +
              " chickens.")

        # set loop variable such that it does not activate
        identifier = 0

    else:
        # display error message
        print("That's too many chickens for every person.")

        # set loop variable such that it activates
        identifier = 1

    # check to see if loop variable is activated
    if identifier == 0:
        break
