num = 34185
large = 0
while num>0:
    rem = num%10
    if rem > large:
        large = rem
    num//=10

print(large)