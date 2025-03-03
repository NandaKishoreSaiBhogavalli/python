def is_leap(year):
    # If the year is divisible by 400, it's a leap year
    if year % 400 == 0:
        return True
    # If the year is divisible by 100 but not 400, it's not a leap year
    elif year % 100 == 0:
        return False
    # If the year is divisible by 4 but not 100, it's a leap year
    elif year % 4 == 0:
        return True
    # Otherwise, it's not a leap year
    else:
        return False
year = int(input())
print(is_leap(year))