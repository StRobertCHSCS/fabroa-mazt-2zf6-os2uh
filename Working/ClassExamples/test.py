print("This program will determine whether or not a number you enter is prime")
input("Press enter to continue")

# Looping the entire program
while True:

    # Determining the number needed to be calculated
    n = int(input("Input your number: "))

    # Setting a "testing" variable- this variable is used to test whether or
    # not the number is divisible by this variable. If this number is 1, every
    # number inputted will automatically be divisible
    x = 2
    condition = 0
    while x <= n:
        if n == 2:
            condition = 1
            break
        else:
            if n % x == 0:
                condition = 1
                break
            else:
                if x*x >= n:
                    condition = 2
                    break
                else:
                    x += 1
       
    if condition == 1:
        print("Your number is not prime.")
    else:
        if condition == 2:
            print("Your number is prime.")
        else:
            print("There was an error")
    b = input("Press enter to input another prime")
