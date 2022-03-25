class Person:
    def __init__(self, first_name: str, last_name: str, email: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email


class Customer(Person):
    def __init__(self, first_name: str, last_name: str, email: str, customer_number: str):
        Person.__init__(self, first_name, last_name, email)
        self.__customer_number = customer_number

    @property
    def customer_number(self):
        return self.__customer_number


class Employee(Person):
    def __init__(self, first_name: str, last_name: str, email: str, ssn: str):
        Person.__init__(self, first_name, last_name, email)
        self.__ssn = ssn

    @property
    def ssn(self):
        return self.__ssn


def main():
    print("Customer/Employee Data Entry\n")
    keep_going = "y"
    while keep_going == "y":
        choice = input("Customer or employee? (c/e): ")
        if choice == "c":
            print("\nDATA ENTRY")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            customer_number = input("Number: ")
            customer = Customer(first_name, last_name, email, customer_number)
            print("\nCUSTOMER")
            print("First name: " + customer.first_name)
            print("Last name: " + customer.last_name)
            print("Email: " + customer.email)
            print("Number: " + customer.customer_number)
            print()
        elif choice == "e":
            print("\nDATA ENTRY")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            ssn = input("SSN: ")
            employee = Employee(first_name, last_name, email, ssn)
            print("\nEMPLOYEE")
            print("First name: " + employee.first_name)
            print("Last name: " + employee.last_name)
            print("Email: " + employee.email)
            print("SSN: " + employee.ssn)
            print()
        else:
            print("Wrong choice selected")

        keep_going = input("Continue? (y/n): ")
        if keep_going == "n":
            print("\nBye!")
            break


if __name__ == "__main__":
    main()
