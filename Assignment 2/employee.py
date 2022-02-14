class Employee:
    def __init__(self, first_name: str, last_name: str, employee_id: str, salary: float):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__employee_id = employee_id
        self.__salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def annual_salary(self):
        return self.__salary * 12

    @property
    def name(self):
        return f"{self.__first_name} {self.__last_name}"

    def raise_salary(self):
        percent = float(input("Raise salary by specified percent: "))
        decimal = percent/100
        added_amount = decimal * self.__salary
        new_salary = added_amount + self.__salary
        self.__salary = new_salary
        print("New salary is now", new_salary)
