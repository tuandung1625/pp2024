def student_infor():
    id = input("Enter student's ID :")
    name = input("Enter student's name :")
    dob = input("Enter student's date of birth : ")
    return {"id" : id, "name" : name, "dob" : dob}

def course_infor():
    course_id = input("Course's ID is : ")
    course_name = input("Course's name is : ")
    return {"id" : course_id, "name" : course_name}

def num_of_students():
    num = int(input("Enter the number of students in a class :"))
    student = []
    for i in range(num):
        temp = student_infor()
        student.append(temp)
    return student

def num_of_course():
    num = int(input("Enter the number of courses :"))
    course = []
    for i in range(num):
        temp = course_infor()
        course.append(temp)
    return course

def list_courses(courses):
    print("\n---List of courses---")
    for course in courses:
        print("ID : {}, name : {}" .format(course['id'], course['name']))

def list_students(students):
    print("\n---List of students---")
    for student in students:
        print("ID : {}, name : {}, dob : {}" .format(student['id'], student['name'], student['dob']))

def input_marks(students, courses, marks):
    list_courses(courses)
    print("Select the course id : ")
    course = input()
    if course not in marks:
        marks[course] = {}

    list_students(students)
    print("Select student id to input mark : ")
    student = input()

    marks[course][student] = float(input("Enter mark : "))
    return marks

def show_marks(students, marks):
    course = input("What course would you want to see : ")
    
    if course not in marks or marks[course] == {}:
        print("This code haven't entered the mark")
    else:
        for student in students:
            if (student["id"] in marks[course]):
                print("Student id : {}, Mark : {}".format(student["id"], marks[course][student["id"]]))
            else:
                print("Student id : {}, Mark : Not entered".format(student["id"]))

marks = {}

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
        students = num_of_students()
    elif (choice == 2):
        courses = num_of_course()
    elif (choice == 3):
        list_courses(courses)
    elif (choice == 4):
        list_students(students)
    elif (choice == 5):
        marks = input_marks(students,courses, marks)
    elif (choice == 6):
        show_marks(students, marks)
    else:
        print("Invalid choice")