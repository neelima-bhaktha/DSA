class Parent:
    def __init(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password

class Child(Parent):
    def __init__(self, name, age, password):
        super().__init__(name, age, password)

