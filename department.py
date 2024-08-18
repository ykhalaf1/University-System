class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []
        self.courses = []

    def add_professor(self, professor):
        self.professors.append(professor)
        print("Professor successfully added!")

    def add_course(self, course):
        self.courses.append(course)
        print("Course successfully added!")

    def display_info(self):
        print(f"\n Department: {self.name}")

        if self.professors:
            print("Professors: ")
            for professor in self.professors:
                professor.display_info()
        else:
            print("No professors in this department")

        if self.courses:
            print("\nCourses: ")
            for course in self.courses:
                course.display_info()
        else:
            print("No courses in this department")
