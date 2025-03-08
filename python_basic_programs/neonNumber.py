num = 9
squares = num*num
add = 0
while squares>0:
    rem = squares%10
    add+=rem
    squares//=10
if add == num:
    print(f"{num} is a neon number")
else:
    print(f"{num} is not a neon number")