def replace_artist(top_artists):
    try:
        index = int(input("Enter the artist you want to replace: "))

        new_artist = input("Enter the new artist name: ")

        top_artists[index] = new_artist
        print(f"{index} has been replaced with {new_artist}.")
    
    except ValueError:
        print("ValueError: Please enter a valid name for the list.")
    
    except IndexError:
        print("IndexError: The name you entered is out of range.")

top_artists = ["Adele", "Drake", "Beyoncé", "Taylor Swift", "Ed Sheeran"]
print("Original top artists list:", top_artists)

replace_artist(top_artists)
print("Updated top artists list:", top_artists)