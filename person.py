class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_ID):
        super().__init__(name, age)
        self.student_ID = student_ID
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)  # Add student to the course's list of students
            print("Course successfully added!")
        else:
            print(f"Already enrolled in {course.course_name}!")

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_ID}")
        if self.courses:
            print("Enrolled Courses: ")
            for course in self.courses:
                print(f" - {course.course_name}")
        else:
            print("No courses enrolled")


class Professor(Person):
    def __init__(self, name, age, professor_ID):
        super().__init__(name, age)
        self.professor_ID = professor_ID
        self.courses = []

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print("Course successfully assigned!")
        else:
            print(f"Already assigned to {course.course_name}!")

    def display_info(self):
        print(f"\nProfessor Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Professor ID: {self.professor_ID}")
        if self.courses:
            print("Courses they teach: ")
            for course in self.courses:
                print(f" - {course.course_name}")
        else:
            print("This professor teaches no courses!")

