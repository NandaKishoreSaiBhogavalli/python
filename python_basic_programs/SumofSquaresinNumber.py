num = 124
sums = 0
while num>0:
    rem = num%10
    sq = rem*rem
    sums+=sq
    num = num//10
print(sums)