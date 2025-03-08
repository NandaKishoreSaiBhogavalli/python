num = 34185
small = float("inf")
while num>0:
    rem = num%10
    if rem < small:
        small = rem
    num//=10

print(small)