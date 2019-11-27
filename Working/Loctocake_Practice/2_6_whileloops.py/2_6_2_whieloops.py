n = int(input("Enter a number: "))
i = 2
while i <= n:
    if (n/i) == float(n//i):
        print(i)
        break
    else:
        i += 1