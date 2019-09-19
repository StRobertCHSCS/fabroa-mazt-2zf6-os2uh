# 1_2_2_operators.py
# There is an error using operators due to the fact that the variable age is
# not a string variable. Using the function str(), we can get around this by
# making the variable age a string variable.

instrument = "kazoo"
age = 7

print("I have played the " + instrument + " since I was " + str(age) + " years old")
