class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def get_age(self):
        return self.__age #double underscore a variable to make it private
p1 = Person("emily", 25)
print(p1.name)
print(p1.get_age()) #this will cause error