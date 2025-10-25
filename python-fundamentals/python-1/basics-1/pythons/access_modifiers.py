class Employee:
    "Common base class for all employees"
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age #public variable
        self.__position = position #private variable
        self._salary = salary #protected variable

    def displayEmployee(self):
        print(f"Name: {self.name} - Age: {self.age} - Position: {self.__position} - Salary: {self._salary}")

e1 = Employee("John", 24, 'Manager',245000)
print(e1.name)
print(e1.age)
print(e1._salary)
# print(e1.__position) [raise attribute error]

# Name Mangling
print(e1._Employee__position)

