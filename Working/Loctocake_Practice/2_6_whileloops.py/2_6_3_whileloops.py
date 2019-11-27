a = int(input("Enter a number: "))
i = 0
while True:
    if 2**i > a:
        i -= 1
        break
    else:
        i += 1
print("exponent: " + str(i))
print("2**n: " + str(2**i))