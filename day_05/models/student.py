from .person import person

class Student(person):
    def __init__(self, usn, Class, dpt):
        self.usn = usn
        self.Class = Class
        self.dpt = dpt
        