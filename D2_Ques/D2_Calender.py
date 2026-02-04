""" 
To check whether a. Year is a leap year or not
                 b. Print the next date in the calendar given the current date
"""
year= int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")
day= int(input("Enter day: "))
month= int(input("Enter month: "))
year= int(input("Enter year: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    days_in_month= 31
elif month in [4, 6, 9, 11]:
    days_in_month= 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month= 29
    else:
        days_in_month= 28
else:
    print("Invalid month")
    exit()
if day < days_in_month:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is: ",day,"-",month,"-",year)
