n1 = 10
n2 = 20
for i in range(n1,n2):
    for j in range(2,i//2):
        if i % j == 0:
            print(f"{i} is not a prime number!")
            break
    else:
        print(f"{i} is a prime number")