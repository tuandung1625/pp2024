class Class(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self, id, name):
        return f"ID : {self.id}, NAME : {self.name}"

class Student(Class):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob

    def show(self):
        print(super().show(id, name) + f", date of birth : {self.dob}")
        
class Course(Class):
    def __init__(self, id, name):
        super().__init__(id, name)
    
    def show(self):
        print(super().show(id,name))

class Mark(object):
    def __init__(self, student_id, course_id):
        self.__student_id = student_id
        self.__course_id = course_id

    def set_mark(self, mark):
        self.__mark = mark

    def get_student_id(self):
        return self.__student_id
    def get_course_id(self):
        return self.__course_id
    def get_mark(self):
        return self.__mark

students = []
courses = []
marks = []

while (True):
    print("---ENTER YOUR CHOICE---")
    print("--0. EXIT THE PROGRAM--")
    print("--1. INPUT STUDENTS----")
    print("--2. INPUT COURSES-----")
    print("--3. LIST COURSES------")
    print("--4. LIST STUDENTS-----")
    print("--5. INPUT MARK--------")
    print("--6. SHOW MARK---------\n")

    choice = int(input())
    if (choice == 0):
        break
    elif (choice == 1):
        if len(students) == 0:
            number_of_student = int(input("Enter the number of students : "))
        else:
            number_of_student = int(input("Enter the number of additional students : "))
        for i in range(number_of_student):
            id = input("Enter student's ID : ")
            if id not in [student.id for student in students]:
                name = input("Enter student's name : ")
                dob = input("Enter student's date of birth : ")
                students.append(Student(id,name,dob))
            else:
                print("Student ID already exists")

    elif (choice == 2):
        if len(courses) == 0:
            number_of_course = int(input("Enter the number of courses : "))
        else:
            number_of_course = int(input("Enter the number of additional courses : "))
        for i in range(number_of_course):
            id = input("Enter course's ID : ")
            if id not in [course.id for course in courses]:
                name = input("Enter course's name : ")
                courses.append(Course(id,name))
            else:
                print("Course ID already exists")

    elif (choice == 3):
        print("List of courses : ")
        for course in courses:
            course.show()

    elif (choice == 4):
        print("List of students : ")
        for student in students:
            student.show()

    elif (choice == 5):
        print("List of courses : ")
        for course in courses:
            course.show()
        course_id = input("Select course id to input mark : ")
        if course_id not in [course.id for course in courses]:
            print("Invalid course id")
            continue

        print("List of students : ")
        for student in students:
            student.show()
        student_id = input("Select student id to input mark : ")
        if student_id not in [student.id for student in students]:
            print("Invalid student id")
            continue

        markk = float(input("Enter mark : "))

        existing_mark = 0
        for mark in marks:
            if mark.get_student_id() == student_id and mark.get_course_id() == course_id:
                existing_mark = mark 
                break
        if (existing_mark != 0):
            existing_mark.set_mark(markk)
        else:
            mark = Mark(student_id, course_id)
            mark.set_mark(markk)
            marks.append(mark)
        
    elif (choice == 6):
        course_id = input("Select course id to show mark :")
        for course in courses:
            if course.id == course_id:
                print("Course name : {}".format(course.name))
        for mark in marks:
            if mark.get_course_id() == course_id:
                print("Student id : {}, Mark : {}".format(mark.get_student_id(), mark.get_mark()))

    else:
        print("Invalid choice")