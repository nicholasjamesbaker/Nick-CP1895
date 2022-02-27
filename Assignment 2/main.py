from circle import Circle
from point import Point
from line import Line
from rectangle import Rectangle
from date import Date
from student import Student
from employee import Employee
from bank import BankAccount
from classtransaction import Transaction

circle1 = Circle(4, "blue")
print("Circle info")
print(circle1.get_area())
print(circle1.get_circumference())
print(circle1)
print()

point1 = Point(4, 0)
point2 = Point(6, 6)

print("Point info")
print(point1)
print(point2)
print()

line1 = Line(point1, point2)
print("Line info")
print(line1.start_point)
print(line1.end_point)
print("LINE LENGTH", line1.length)
print()

rectangle1 = Rectangle(point1, point2)
print("Rectangle info")
print(rectangle1.area)
print(rectangle1.perimeter)
print()

date1 = Date(24, 7, 1998)
print("Date info")
print(date1)
print(date1.is_leap_year)
print(date1.is_valid_date)
print()

student1 = Student(20087324, "Nicholas Baker", "Beast Street", "ASD", ["Python", "Java", "JavaScript"], {'Systems': 90, 'Security': 85})
print("Student info")
print("Average score is", student1.average_score)
print()

employee1 = Employee("Nick", "Baker", "E0001", 4000)
print("Employee info")
print(employee1.name)
print(employee1.annual_salary)
print()

print("Bank Account/Transaction Info")
nick_account = BankAccount("Nick", 2000, [])
rick_account = BankAccount("Rick", 3000, [])
transaction1 = Transaction(nick_account, rick_account, 1000)
print("Rick Account Balance (After transaction 1):", rick_account.balance)
print("Nick Account Balance (After transaction 1):", nick_account.balance)
transaction2 = Transaction(rick_account, nick_account, 3500)
print("Rick Account Balance (After transaction 2):", rick_account.balance)
print("Nick Account Balance (After transaction 2):", nick_account.balance)
transaction3 = Transaction(nick_account, rick_account, 4500)
print("Rick Account Balance (After transaction 3):", rick_account.balance)
print("Nick Account Balance (After transaction 3):", nick_account.balance)
