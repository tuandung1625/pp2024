class Class(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        return f"ID : {self.id}, NAME : {self.name}"

class Student(Class):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob

    def set_gpa(self, gpa):
        self.gpa = gpa
    
    def show(self):
        return super().show() + f", date of birth : {self.dob}"
        
class Course(Class):
    def __init__(self, id, name, credit):
        super().__init__(id, name)
        self.credit = credit
    
    def show(self):
        return super().show() + f", credit : {self.credit}"