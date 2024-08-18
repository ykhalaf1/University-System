class Course:
    def __init__(self, course_name, professor):
        self.course_name = course_name
        self.professor = professor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} successfully added to {self.course_name}!")
        else:
            print(f"Student {student.name} is already enrolled in {self.course_name}!")

    def display_info(self):
        print(f"\nCourse Name: {self.course_name}")
        print(f"Professor: {self.professor.name}")
        if self.students:
            print("Students enrolled: ")
            for student in self.students:
                print(f" - {student.name}")
        else:
            print("No students enrolled!")