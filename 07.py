class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self._ssn = ssn

emp =  Employee("john", 5000, "123-45-6789")         
print(emp.name)
print(emp._salary)
print(emp._Employee_ssn)