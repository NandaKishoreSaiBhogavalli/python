a = 3
b = 8
c = 10
if a>b:
    print(f"{a} is greater than {b}")            #greatest of two numbers
else:
    print(f"{b} is greater than {a}")


if a > b and a > c:
    print(f"{a} is the greatest among {a}, {b}, and {c}")                          #greatest of three numbers
elif b > c:
    print(f"{b} is the greatest among {a}, {b}, and {c}")
else:
    print(f"{c} is the greatest among {a}, {b}, and {c}")