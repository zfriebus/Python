
class Employee:
    def __init__(self, name, number):
        self.number = number
        self.name = name

    def __str__(self):
        return f"Employee: Color: {self.name}, Employee number: {self.number}"


class ProductionWorker(Employee):
    def __init__(self, shift_number, hourly_pay_rate):
        super().__init__(shift_number, hourly_pay_rate)


def main():

    print("\n\n")
    Zach = Employee("Zach", "13")
    print("Zach: ")
    print(Zach)

    print("\n\n")
    print("Jacob:")
    Jacob = ProductionWorker("12", "18/hr")
    print(Jacob)
    print("\n\n")


main()