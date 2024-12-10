def main_menu():
        print("Menu:")
        while True:
            try:
                print("\\nWelcome! You can take notes, change usernames, delete notes, or display notes.")
                print("1. Create a new notes")
                print("2. Display an entry by username")
                print("3. Update existing notes")
                print("4. Remove notes")
                print("5. Quit")
                choice = int(input("Please enter the number of your selection: "))
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("That is not a valid number. Try again.")
            except ValueError:
                print("That is not a valid number. Try again.")
def check():
        print("Checking the system...")

def create():
        print("Creating new notes...")

def read():
        print("Reading notes...")

def update():
        print("Updating notes...")

def delete():
        print("Deleting notes entry...")

def check():
    try:
        file = open("user_notes.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
     print("user notes does not exist. Creating new notes...")
    return []

def create():
        user = check()
        fname = input("Please enter the users\'s first name: ")
        lname = input("Please enter the users\'s last name: ")
        date = input("Please enter the date: ")
        time = input("Please enter the time: ")
        entry = f"{fname}, {lname}, {date}, {time}\\n"
        user.append(entry)
        save(user)

def save(output):
        file = open("user_notes.txt", 'w')
        for line in output:
            file.write(line)
        file.close()
        print("File updated.")
    

create()