total_numbers = int(input())
n = 0
p = []
q = []
for x in range(1, total_numbers + 1):
    p.append(int(input()))
for i in p:
    for y in range(2, i):
        if i % y == 0:
            q.append(i//y)
        else:
    for z in q:
        sum_z += z
    if sum_z <= i:
        print(str(i) + " is a deficient number.")
    else:
        if sum_z == i:
            print(str(i) + " is a perfect number.")
        else:
            if sum_z >= i:
                print(str(i) + " is an abundant number.")


            

            
    
