import random
ran_number = random.randrange(1, 100)


def mainfunc(ran_number):
    num_guess = int(input("Guess a number 1-100: "))
    difference = ran_number - num_guess
    absolute_value = abs(difference)
    while absolute_value != 0:
        if absolute_value <= 5:
         print("You are very hot")
         num_guess = int(input("Guess a number 1-100: "))
         difference = ran_number - num_guess
         absolute_value = abs(difference)
        elif absolute_value <= 15 and absolute_value > 5:
         print("You are hot")
         num_guess = int(input("Guess a number 1-100: "))
         difference = ran_number - num_guess
         absolute_value = abs(difference)
        elif absolute_value <= 25 and absolute_value > 15:
         print("You are cool")
         num_guess = int(input("Guess a number 1-100: "))
         difference = ran_number - num_guess
         absolute_value = abs(difference)
        elif absolute_value > 25:
         print("You are cold")
         num_guess = int(input("Guess a number 1-100: "))
         difference = ran_number - num_guess
         absolute_value = abs(difference)
    print("You are correct!!!!!")    
         
        

    
mainfunc(ran_number)
