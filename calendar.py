from calendar import calendar
from datetime import datetime

def main():
 datetime.datetime.now().year

 month = int(input("What Month were you born (as a number. May would be 5)  "))
 if 1 <= month <= 12:
    return month 
 else:
  print("Invalid input. Please enter a number between 1 and 12.")


 print(calendar(2024, month))
