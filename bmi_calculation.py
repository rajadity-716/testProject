#LeapYear Code
year=int(input("Enter any year\n"))
if year%4==0 or year%400==0:
    print(f"Year {year} is a leap year!")
else:
    print(f"Year{year} is a non-leap year!")