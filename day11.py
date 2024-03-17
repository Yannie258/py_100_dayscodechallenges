# ''' how many seconds in a year / leap year
"""
- user inputs year
- check the year is normal or leap
  second_a_day=  24*60*60 seconds
  if(leap)
     366*second_a_day
  else:
      365*second_a_day
"""

year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(year, "is a leap year")
  second_a_day = 24 * 60 * 60
  print("There are", 366 * second_a_day, "seconds in a leap year")
else:
  print(year, "is not a leap year")
  second_a_day = 24 * 60 * 60
  print("There are", 365 * second_a_day, "seconds in a normal year")