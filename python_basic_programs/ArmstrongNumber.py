num = 153
original = num
sums = 0
while num>0:
    rem = num%10
    cube = rem**3
    sums+=cube
    num = num//10
if original == sums:
    print("armstrong number")
else:
    print("not a armstrong number")