num = 123
Original = num
mul = 1
add = 0
while num>0:
    rem = num%10
    mul = mul*rem
    add = add+rem
    num//=10
if mul == add:
    print(f"{Original} is a spy Number")
else:
    print(f"{Original} is not a spy Number")