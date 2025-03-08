nums = 34216
rev = 0
while nums>0:
    rem = nums%10
    rev = (rev*10)+rem
    nums//=10
while rev>0:
    remainder = rev%10
    if rev%2==0:
        print(remainder,end=",")
    rev//=10
