
nato_alphabet = {
    "A": "Alpha",
    "b": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliette",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-Ray",
    "Y": "Yankee",
    "Z": "Zulu",
}


def Main():
 Inp_name = input ("Enter a word: ")
 name = Inp_name.upper()
 for key in name:
    print(key, nato_alphabet[key])

Main()