class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind 
        self._breed = breed
        self._name = name

    
    def get_kind(self):
        self._kind = input("Enter the kind of animal: ")
        return self._kind

    def set_kind(self, kind):
        self._kind = kind

    
    def get_breed(self):
        self._breed = input("Enter a breed: ")
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    
    def get_name(self):
       self._name =  input("Enter a name: ")
       return self._name

    def set_name(self, name):
        self._name = name

    
    def print_details(self):
        print(f"Kind: {self._kind}, Breed: {self._breed}, Name: {self._name}")



pet1 = Pet("Dog", "Husky", "Sadie")
pet2 = Pet("Cat", "Persian", "Oscar")
pet3 = Pet("Bird", "Parrot", "Blue")


pet1.print_details()
pet2.print_details()
pet3.print_details()


print(f"The name of the pet is: {Pet.__name__}")


