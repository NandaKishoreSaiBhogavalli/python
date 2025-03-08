num = 12
sums = 0
for i in range(1,num):
    if num%i==0:
        print(f"Factor of {num} is {i}")
        sums+=i
    else:
        pass
if num==sums:
    print("it is a perfect number")
else:
    print("not a perfect number")