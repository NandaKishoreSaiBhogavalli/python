# 1+8 = 9,  18%9==0 so harshad number
num = 18
original = num
sums = 0
while num>0:
    rem = num%10
    sums+=rem
    num//=10
if original%sums==0:
    print("harshad number")
else:
    print("not a harshad number")