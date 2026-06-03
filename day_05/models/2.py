class Student:
    def __init__(self, name, grade):
        self.name  = name
        self.grade  = grade


    def __str__(self):
        return f"{self.name} {self.grade}"
s1 = Student("ANNA", "A")
print(s1)
# s1.grade="B"
# print(s1.grade)