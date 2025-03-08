num = 212
original = num
reverse = 0
while num>0:
    rem = num%10
    reverse = reverse*10+rem
    num = num//10
if original==reverse:
    print(f"It is a palindrome")
else:
    print(f"It is not a palindrome")