class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, emp):
        self.emp = emp

    def show_employee(self):
        print(f"Department has employee: {self.emp.name}")