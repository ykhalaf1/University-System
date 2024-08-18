from person import Student, Professor
from course import Course
from department import Department
from university import University

university = University()

while True:
    print("\nUniversity Management System:")
    print("1. Add Student")
    print("2. Add Professor")
    print("3. Add Department")
    print("4. Add Course")
    print("5. Enroll Student in a Course")
    print("6. List Students")
    print("7. List Professors")
    print("8. List Departments")
    print("9. Exit")

    choice = int(input("Make a selection: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        student_ID = int(input("Enter Student ID: "))
        student = Student(name, age, student_ID)
        university.add_student(student)
        print(f"Student {name} added successfully!")

    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        professor_ID = int(input("Enter Professor ID: "))
        professor = Professor(name, age, professor_ID)
        university.add_professor(professor)
        print(f"Professor {name} added successfully!")

    elif choice == 3:
        department_name = input("Enter Department Name: ")
        department = Department(department_name)
        university.add_department(department)

    elif choice == 4:
        department_name = input("Enter Department Name for the Course: ")
        course_name = input("Enter Course Name: ")
        professor_name = input("Enter Professor's Name: ")

        department = None
        for dept in university.departments:
            if dept.name == department_name:
                department = dept
                break

        professor = None
        for prof in university.professors:
            if prof.name == professor_name:
                professor = prof
                break

        if department and professor:
            course = Course(course_name, professor)
            department.add_course(course)
            professor.assign_course(course)
            print(f"Course {course_name} added to Department {department_name} successfully!")
        else:
            print("Invalid department or professor.")

    elif choice == 5:  # Enroll student in a course
        student_name = input("Enter Student's Name: ")
        course_name = input("Enter Course Name: ")

        student = None
        for stud in university.students:
            if stud.name == student_name:
                student = stud
                break

        course = None
        for dept in university.departments:
            for crs in dept.courses:
                if crs.course_name == course_name:
                    course = crs
                    break

        if student and course:
            student.enroll(course)  # Enroll student in course
            print(f"Student {student_name} enrolled in {course_name} successfully!")
        else:
            print("Invalid student or course.")


    elif choice == 6:
        university.list_students()

    elif choice == 7:
        university.list_professors()

    elif choice == 8:
        university.list_departments()

    elif choice == 9:
        print("Exiting system.")
        break

    else:
        print("Invalid choice, please try again.")
