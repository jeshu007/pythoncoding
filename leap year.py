def is_leap_year(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

year = int(input("enter a year:"))
if is_leap_year(year):
    print(year,"is a leap year:")
else:
    print(year,"is not a leap year:")
