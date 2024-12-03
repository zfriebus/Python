from datetime import datetime

def main():
   
    print("\n\n")
    try:
        # gets user info
        today = datetime.today()
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 
    # finds how old in days user is
        delta = today - birthday
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425
        total_days = delta.days
       # prints user age
        print(f'You are {delta_years} years old')

        months = total_days // 30.44
        print(f" - {int(months):,} months")

        weeks = total_days // 7
        print(f" - {int(weeks):,} weeks")
        
      # tells user when a incorrect input entered
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()