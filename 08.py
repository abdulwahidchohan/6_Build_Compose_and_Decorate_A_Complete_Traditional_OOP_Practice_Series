class Person():
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subjects):
        super().__init__(name)        
        self.subjects = subjects