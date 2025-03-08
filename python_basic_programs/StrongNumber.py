import math
num = 145
original = num
sums = 0
while num>0:
    div = num%10
    fact = math.factorial(div)
    sums+=fact
    num = num//10
if original == sums:
    print("Strong number")
else:
    print("Not a Strong number")
#145 = 1! + 4! + 5! = 145