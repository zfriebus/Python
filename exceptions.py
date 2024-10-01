def square_number():
    number = input("Enter a number to square: ")
    squared_number = int(number) ** 2
    print(f"The square of {number} is {squared_number}.")
    return number
square_number()
try: 
    number = .1
except ValueError:
    print("Invalid value inputed!")
else:
    print("square completed!")
finally:
    print("Execution completed.")
