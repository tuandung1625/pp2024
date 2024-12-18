from math import floor
import numpy

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

    def set_gpa(self, gpa):
        self.gpa = gpa
    
    def show(self):
        print(super().show(self.id, self.name) + f", date of birth : {self.dob}")
        
class Course(Class):
    def __init__(self, id, name, credit):
        super().__init__(id, name)
        self.credit = credit
    
    def show(self):
        print(super().show(self.id,self.name) + f", credit : {self.credit}")

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

class University(object):
    def __init__(self, students, courses, marks):
        self.students = students
        self.courses = courses
        self.marks = marks

    def input_student(self):
        if len(self.students) == 0:
            number_of_student = int(input("Enter the number of students : "))
        else:
            number_of_student = int(input("Enter the number of additional students : "))
        for i in range(number_of_student):
            id = input("Enter student's ID : ")
            if id not in [student.id for student in self.students]:
                name = input("Enter student's name : ")
                dob = input("Enter student's date of birth : ")
                self.students.append(Student(id,name,dob))
            else:
                print("Student ID already exists")

    def input_course(self):
        if len(self.courses) == 0:
            number_of_course = int(input("Enter the number of courses : "))
        else:
            number_of_course = int(input("Enter the number of additional courses : "))
        for i in range(number_of_course):
            id = input("Enter course's ID : ")
            if id not in [course.id for course in self.courses]:
                name = input("Enter course's name : ")
                credit = float(input("Enter course's credit : "))
                self.courses.append(Course(id,name,credit))
            else:
                print("Course ID already exists")
    
    def input_mark(self):
        print("List of courses : ")
        for course in self.courses:
            course.show()
        course_id = input("Select course id to input mark : ")
        if course_id not in [course.id for course in self.courses]:
            print("Invalid course id")
            return

        print("List of students : ")
        for student in self.students:
            student.show()
        student_id = input("Select student id to input mark : ")
        if student_id not in [student.id for student in self.students]:
            print("Invalid student id")
            return
        
        markk = float(input("Enter mark : "))
        markk = floor(markk*10)/10

        existing_mark = 0
        for mark in self.marks:
            if mark.get_student_id() == student_id and mark.get_course_id() == course_id:
                existing_mark = mark 
                break
        if (existing_mark != 0):
            existing_mark.set_mark(markk)
        else:
            mark = Mark(student_id, course_id)
            mark.set_mark(markk)
            self.marks.append(mark)
    
    def show_student(self):
        print("List of students : ")
        for student in self.students:
            student.show()

    def show_course(self):
        print("List of courses : ")
        for course in self.courses:
            course.show()

    def show_mark(self):
        course_id = input("Select course id to show mark :")
        for course in self.courses:
            if course.id == course_id:
                print("Course name : {}".format(course.name))
        for mark in self.marks:
            if mark.get_course_id() == course_id:
                print("Student id : {}, Mark : {}".format(mark.get_student_id(), mark.get_mark()))

    def show_gpa(self):
        credits = numpy.array([course.credit for course in self.courses])
        for student in self.students:
            scores = numpy.array([mark.get_mark() for mark in self.marks if mark.get_student_id() == student.id])
            weighted_sum = numpy.sum(credits * scores)
            gpa = weighted_sum/numpy.sum(credits)
            student.set_gpa(gpa)
        students_sorted = sorted(self.students, key=lambda x: x.gpa, reverse=True)
        for student in students_sorted:
            print("Student name: {}, GPA: {:.2f}".format(student.name, student.gpa))
    
    def execute(self):
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
            print("--6. SHOW MARK---------")
            print("--7. SHOW GPA----------\n")

            choice = int(input())
            if (choice == 0):
                break
            elif (choice == 1):
                self.input_student()
            elif (choice == 2):
                self.input_course()
            elif (choice == 3):
                self.show_course()
            elif (choice == 4):
                self.show_student()
            elif (choice == 5):
                self.input_mark()
            elif (choice == 6):
                self.show_mark()
            elif (choice == 7):
                self.show_gpa()
            else:
                print("Invalid choice")

SGP = University([],[],[])
SGP.execute()