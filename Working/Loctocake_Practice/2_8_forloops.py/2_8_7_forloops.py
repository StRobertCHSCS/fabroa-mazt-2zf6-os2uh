i = 1
a = 0
while i <= 3:
    a += float(input("Please the price of the product " + str(i) + ": ")) * int(input("Please enter the quantity of product " + str(i) + ": "))
    i += 1
print(str(round(a * 1.13, 2)))