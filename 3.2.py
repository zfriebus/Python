class Person:
    def __init__(self, name, address, age, phoneNumber):
        self.__name = name  
        self.__address = address    
        self.__age = age    
        self.__phoneNumber = phoneNumber           
    def get_info(self):
        return f"{self.__name} {self.__address}, age: {self.__age}, phonenumber: {self.__phoneNumber}"

    
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self._name = name
        print(name)
    
    def set_address(self, address):
        self.__address = address
        print(address)

    def set_age(self, age):
        self.__age = age
        print(age)
    
    def set_phoneNumber(self, phonenumber):
        self.__phoneNumber = phonenumber
        print(phonenumber)
