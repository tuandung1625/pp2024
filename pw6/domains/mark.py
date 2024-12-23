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