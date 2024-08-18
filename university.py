class University:
    def __init__(self):
        self.students = []
        self.professors = []
        self.departments = []

    def add_student(self, student):
        self.students.append(student)
        print("Student successfully added!")

    def add_professor(self, professor):
        self.professors.append(professor)
        print("Professor successfully added!")
    
    def add_department(self, department):
        self.departments.append(department)
        print("Department successfully added!")

    def list_students(self):
        if self.students:
            for student in self.students:
                student.display_info()
        else:
            print("No students in the system.")

    def list_professors(self):
        if self.professors:
            for professor in self.professors:
                professor.display_info()
        else:
            print("No professors in the system.")

    def list_departments(self):
        if self.departments:
            for department in self.departments:
                department.display_info()
        else:
            print("No departments in the system.")
