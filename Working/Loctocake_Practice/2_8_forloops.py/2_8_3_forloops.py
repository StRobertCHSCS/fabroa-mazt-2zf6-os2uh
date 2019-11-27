a = int(input("Enter start: "))
b = int(input("Enter end: "))

if a <= b:
    i = a
    while i <= b:
        print(str(i))
        i += 1
else:
    print("Invalid values")