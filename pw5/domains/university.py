import curses
from domains.base_class import Student, Course
from domains.mark import Mark
import numpy
from math import floor
import os
from domains.file_handle import FileHandle

class University(object):
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

        if not os.path.exists("data"):
            os.makedirs("data")

    def write_to_file(self, filename, data):
        filepath = os.path.join("data", filename)
        with open(filepath, "w") as file:
            file.write(data)

    def input_student(self, stdscr):
        stdscr.clear()
        # input number of students
        if len(self.students) == 0:
            stdscr.addstr(0,0, "Enter the number of students : ")
            curses.echo()
            number_of_student = int(stdscr.getstr().decode())
        else:
            stdscr.addstr(0,0, "Enter the number of additional students : ")
            curses.echo()
            number_of_student = int(stdscr.getstr().decode())
        
        # input student's information
        length = 0
        for i in range(number_of_student):
            length += 1
            stdscr.addstr(length,0, "Enter student's ID : ")
            curses.echo()
            id = stdscr.getstr().decode()

            while (id in [student.id for student in self.students]):
                stdscr.addstr(length + 1,0, "Student ID already exists", curses.color_pair(2))
                stdscr.addstr(length + 2,0, "Enter student's ID : ")
                curses.echo()
                id = stdscr.getstr().decode()
                length += 2

            stdscr.addstr(length + 1,0, "Enter student's name : ")
            curses.echo()
            name = stdscr.getstr().decode()
            stdscr.addstr(length + 2,0, "Enter student's date of birth : ")
            curses.echo()
            dob = stdscr.getstr().decode()
            self.students.append(Student(id,name,dob))
            length += 2
        curses.noecho()

        student_data = "\n".join([f"{student.id},{student.name},{student.dob}" for student in self.students])
        self.write_to_file("students.txt", student_data)

    def input_course(self, stdscr):
        stdscr.clear()
        # input number of courses
        if len(self.courses) == 0:
            stdscr.addstr(0,0, "Enter the number of courses : ")
            curses.echo()
            number_of_course = int(stdscr.getstr().decode())
        else:
            stdscr.addstr(0,0, "Enter the number of additional courses : ")
            curses.echo()
            number_of_course = int(stdscr.getstr().decode())

        # input course's information
        length = 0
        for i in range(number_of_course):
            length += 1
            stdscr.addstr(length,0, "Enter course's ID : ")
            curses.echo()
            id = stdscr.getstr().decode()

            while (id in [course.id for course in self.courses]):
                stdscr.addstr(length + 1,0, "Course ID already exists", curses.color_pair(2))
                stdscr.addstr(length + 2,0, "Enter course's ID : ")
                curses.echo()
                id = stdscr.getstr().decode()
                length += 2

            stdscr.addstr(length + 1,0, "Enter course's name : ")
            curses.echo()
            name = stdscr.getstr().decode()
            length += 1

            while True:
                try:
                    stdscr.addstr(length + 1, 0, "Enter course's credit : ")
                    credit = float(stdscr.getstr().decode())
                    self.courses.append(Course(id,name,credit))
                    length += 1
                    break  
                except ValueError:
                    stdscr.addstr(length + 2, 0, "Invalid credit type. Please enter a valid number.", curses.color_pair(2))
                    length += 2
        curses.noecho()

        course_data = "\n".join([f"{course.id},{course.name},{course.credit}" for course in self.courses])
        self.write_to_file("courses.txt", course_data)
    
    def input_mark(self, stdscr):
        # Show list of courses
        stdscr.clear()
        stdscr.addstr(0,0, "List of courses : ")
        for idx, course in enumerate(self.courses):
            stdscr.addstr(idx+1, 0, course.show())
        stdscr.refresh()

        # input and validate course id
        length = len(self.courses) + 1
        while (True):
            stdscr.addstr(length,0,"Select course id to input mark : ")
            curses.echo()
            course_id = stdscr.getstr().decode()
            if course_id not in [course.id for course in self.courses]:
                stdscr.addstr(length + 1,0, "Invalid course id", curses.color_pair(2))
                length += 2
                continue
            break

        # Show list of students
        stdscr.clear()
        stdscr.addstr(0,0, "List of students : ")
        for idx, student in enumerate(self.students):
            stdscr.addstr(idx+1, 0, student.show())
        stdscr.refresh()

        # input and validate student id
        length = len(self.students) + 1
        while (True):
            stdscr.addstr(length, 0, "Select student id to input mark : ")
            curses.echo()
            student_id = stdscr.getstr().decode()
            if student_id not in [student.id for student in self.students]:
                stdscr.addstr(length + 1,0, "Invalid student id", curses.color_pair(2))
                length += 2
                continue
            break
        
        # input and validate mark
        stdscr.clear()
        length = 0
        while (True):
            try:
                stdscr.addstr(length,0, "Enter mark :")
                curses.echo()
                markk = float(stdscr.getstr().decode())
                if markk < 0:
                    stdscr.addstr(length + 1,0, "Invalid mark", curses.color_pair(2))
                    length += 2
                    continue
                break
            except ValueError as e:
                stdscr.addstr(length + 1, 0, f"Invalid mark: {str(e)}", curses.color_pair(2))
                length += 2  
            
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
        curses.noecho()

        mark_data = "\n".join([f"{mark.get_student_id()},{mark.get_course_id()},{mark.get_mark()}" for mark in self.marks])
        self.write_to_file("marks.txt", mark_data)
    
    def show_student(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0,0, "List of students : ")
        for idx, student in enumerate(self.students):
            stdscr.addstr(idx+2,0,student.show())
        stdscr.addstr(len(self.students) + 3,0, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()

    def show_course(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0,0, "List of courses : ")
        for idx, course in enumerate(self.courses):
            stdscr.addstr(idx+2, 0, course.show())
        stdscr.addstr(len(self.courses) + 3,0, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()

    def show_mark(self, stdscr):
        stdscr.clear()
        # input course id to show mark
        stdscr.addstr(0,0,"Select course id to show mark : ")
        curses.echo()
        course_id = stdscr.getstr().decode()

        # show student's mark
        for course in self.courses:
            if course.id == course_id:
                stdscr.addstr(2,0,"Course name : {}".format(course.name))
        length = 3
        for mark in self.marks:
            if mark.get_course_id() == course_id:
                length += 1
                stdscr.addstr(length,0,"Student id : {}, Mark : {}".format(mark.get_student_id(), mark.get_mark()))
        
        curses.noecho()
        stdscr.addstr(len(self.students) + 5,0, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()
        
    def show_gpa(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0,0, "List of students sorted by GPA : ")
        credits = numpy.array([course.credit for course in self.courses])
        for student in self.students:
            scores = numpy.array([mark.get_mark() for mark in self.marks if mark.get_student_id() == student.id])
            weighted_sum = numpy.sum(credits * scores)
            gpa = weighted_sum/numpy.sum(credits)
            student.set_gpa(gpa)
        students_sorted = sorted(self.students, key=lambda x: x.gpa, reverse=True)
        for idx, student in enumerate(students_sorted):
            stdscr.addstr(idx+2,0, student.show() + f", GPA : {student.gpa:.2f}")
        stdscr.addstr(len(self.students) + 3,0, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()
    
    def execute(self, stdscr):
        curses.curs_set(0)  # Hide the cursor
        current_row = 0
        menu = [
            "---ENTER YOUR CHOICE---",
            "0. EXIT THE PROGRAM",
            "1. INPUT STUDENTS",
            "2. INPUT COURSES",
            "3. LIST COURSES",
            "4. LIST STUDENTS",
            "5. INPUT MARK",
            "6. SHOW MARK",
            "7. SHOW GPA"
        ]

        while (True):
            # Display menu
            stdscr.clear()
            for i, option in enumerate(menu):
                if i == current_row:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(i + 2, 0, option)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.addstr(i + 2, 0, option)

            stdscr.refresh()

            # Capture user input
            key = stdscr.getch()
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == ord("\n"):  # Enter key
                if current_row == 1: 
                    FileHandle().exit_program(stdscr)
                    break
                elif current_row == 2:  
                    self.input_student(stdscr)
                elif current_row == 3: 
                    self.input_course(stdscr)
                elif current_row == 4:
                    self.show_course(stdscr)
                elif current_row == 5:
                    self.show_student(stdscr)
                elif current_row == 6:
                    self.input_mark(stdscr)
                elif current_row == 7:
                    self.show_mark(stdscr)
                elif current_row == 8:
                    self.show_gpa(stdscr)
                else:
                    stdscr.addstr(10, 0, "Invalid choice")
                    stdscr.refresh()