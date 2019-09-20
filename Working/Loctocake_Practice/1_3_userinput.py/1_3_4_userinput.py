# 1_3_4_userinput.py
# This program prints, given that the user inputs a number of given apples and
# students, how many apples each student gets and the remaining amount of 
# apples that are not consumed.

print("There are a given number of students and a number of apples that I")
print("have.")

next = input("Press enter to continue")

print("This program will print how many apples each student will get were the")
print("apples split among the students.")

next = input("Press enter to continue")

print("The remaining apples are left over in the basket.")

number_of_students = int(input("Enter the number of students: "))
number_of_apples = int(input("Enter the number of apples: "))

print("Each student gets", number_of_apples//number_of_students, "apples.")
print("There are", number_of_apples % number_of_students, "apples left.")
