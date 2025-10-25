# Static methods = A method that belong to a class rather than any object from that class (instance), Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for general utility functions that do not need access class data
# Class methods = Best for class-level data or require access to the class itself

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Bob", "Manager")
employee2 = Employee("John", "Cashier")
employee3 = Employee("Jenny", "Cook")

print(Employee.is_valid_position("Rocket Scientist"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())