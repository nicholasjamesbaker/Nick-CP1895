class Student:
    def __init__(self, student_id: int, name: str, address: str, program: str, current_courses: list, completed_courses: dict):
        self.__student_id = student_id
        self.__name = name
        self.__address = address
        self.__program = program
        self.__current_courses = current_courses
        self.__completed_courses = completed_courses

    @property
    def name(self):
        return self.__name

    @property
    def student_id(self):
        return self.__student_id

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def average_score(self):
        if not self.__completed_courses:
            return -1
        else:
            filtered_vals = [v for _, v in self.__completed_courses.items() if v != 0]
            average = sum(filtered_vals) / len(filtered_vals)
            return average

    def add_course(self):
        new_course = input("Name of course to be added: ")
        self.__current_courses.append(new_course)
        print(new_course, "has been added to current courses")

    def drop_course(self):
        delete_course = input("Name of course to be deleted: ")
        if delete_course not in self.__current_courses:
            raise ValueError("Course name not in list")
        else:
            self.__current_courses.remove(delete_course)
            print("Updated course list is:", self.__current_courses)

    def course_completed(self):
        course_id = input("Enter name of course: ")
        marks_obtained = int(input("Enter the mark: "))
        if course_id not in self.__current_courses:
            raise ValueError("Course name not in list")
        else:
            self.__completed_courses[course_id] = marks_obtained
            print("Updated course list is:", self.__completed_courses)
