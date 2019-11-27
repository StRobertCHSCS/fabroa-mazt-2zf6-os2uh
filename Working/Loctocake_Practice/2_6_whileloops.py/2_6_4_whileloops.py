a = int(input("Starting distance: "))
b = int(input("Target distance: "))
i = float(a)
c = 1
while i <= float(b):
    i = i*(1.1)
    c += 1
print("You will be ready to run " + str(b) + "km in " + str(c) + " days.")