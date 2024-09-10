Birthday = int(input("Type in 28"))
SportsNumber = int(input("type in 13"))
if Birthday >= 0 and SportsNumber >= 0:
    print("Both numbers are greater than zero.")
if Birthday >= 20 or SportsNumber >= 20:
    print("One is above 20")
if Birthday % 7 == 0 or SportsNumber % 7 ==0:
    print("One number divides by 7")
if Birthday >= SportsNumber:
    print("Birthday is greater than sports number")
if Birthday <= 100 or SportsNumber <= 100:
    print("Both less than 100")
if Birthday <= 50 and SportsNumber <= 50:
    print("Both smaller than 50")