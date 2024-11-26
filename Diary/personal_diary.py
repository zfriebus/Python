def main():
    # this gets the date and time
    current_date_time = input("Enter the current date and time (e.g., 2024-11-25 12:00): ")
    # gets the diary entry
    diary_entry = input("Write your diary entry: ")

    with open("diary.txt", "a") as diary_file:
        diary_file.write(f"Date and Time: {current_date_time}\n")
        diary_file.write(f"Diary Entry: {diary_entry}\n")
        diary_file.write("\n") 
try:
    # Open the file in read mode
    diary_file = open('diary.txt', 'a')
    # Read file content
    content = diary_file.read()
    print(content)
    diary_file.close() 
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
    
print("Your diary entry has been saved.")

main()