class InvalidInputError(Exception):

    def main():
        while True:
            try:
              user_input = input("Enter a number: ")
            
            except InvalidInputError:
             
             if not user_input.isdigit():
                raise InvalidInputError()
            
            finally:
             number = int(user_input)
            print(f"Thank you! You entered the number: {number}")
            break

InvalidInputError()
    