num = 129
sum_of = 1
while num>0:
    rem = num%10
    sum_of *=rem
    num = num//10
print(sum_of)