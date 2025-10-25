# class Shape:
#     def __init__(self, color, filled):
#         self.color = color
#         self.filled = filled
#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.filled else 'not_filled'}")

# class Circle(Shape):
#     def __init__(self, color, filled, radius):
#         super().__init__(color, filled)
#         self.radius = radius
#     def describe(self):
#         super().describe()
#         print(f"It is a circle with area of {3.14 * self.radius * self.radius}cm²")

# class Square(Shape):
#     def __init__(self, color, filled, width):
#         super().__init__(color, filled)
#         self.width = width
#     def describe(self):
#         super().describe()
#         print(f"It is a square with area of {self.width * self.width}cm²")


# class Triangle(Shape):
#     def __init__(self, color, filled, width, height):
#         super().__init__(color, filled)
#         self.width = width
#         self.height = height

#     def describe(self):
#         super().describe()
#         print(f"It is a triangle with area of {(self.width * self.height) /2 }cm²")
        

# circle = Circle(color="red" , filled=True, radius=5)
# square = Square(color="blue" , filled=False, width=6)
# triangle = Triangle(color="yellow" , filled=True, width=6, height=7)

# triangle.describe()
# print(triangle.color)
# print(square.width)
# print(circle.radius)

# from abc import ABC, abstractmethod
# class Shape:
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius**2
    
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return self.base * self.height * 0.5
    
# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping
    
# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza('pepperoni', 15)]

# for shape in shapes:
#     print(f"{shape.area()}cm²")


# class Employee:

#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def get_info(self):
#         return f"{self.name} - {self.position}"
    
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Cook", "Manager", "Waiter", "Cashier", "Chief", "Master"]
#         return position in valid_positions
    
# emp1 = Employee("John", "Manager")
# emp2 = Employee("David", "Cook")
# emp3 = Employee("Eugene", "Cashier")

# print(Employee.is_valid_position("Master"))
# print(Employee.is_valid_position("Cook"))
# print(Employee.is_valid_position("Actor"))

# print(emp1.get_info())
# print(emp2.get_info())
# print(emp3.get_info())


# class Student:
#     count = 0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     def get_info(self):
#         return f"{self.name} - {self.gpa}"
    

#     @classmethod
#     def get_count(cls):
#         return f"Total nr. of students: {cls.count}"
    
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average GPA: {(cls.total_gpa / cls.count):.2f}"
    

# student1 = Student("John", 3.8)
# student2 = Student("Jenny", 3.3)
# student3 = Student("John", 2.90)

# # print(Student.get_count())
# print(Student.get_average_gpa())


    
# class Book:
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         return f"{self.title} - {self.author}"
    
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
    
#     def __lt__(self, other):
#         return self.num_pages < other.num_pages
    
#     def __gt__(self, other):
#         return self.num_pages > other.num_pages
    
#     def __add__(self, other):
#         return self.num_pages + other.num_pages
    
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
    
#     def __getitem__(self, key):
#         if key == "title":
#             return self.title
#         elif key == 'author':
#             return self.author
#         elif key == 'num_pages':
#             return self.num_pages
#         else:
#             return f"Key '{key} was not found.'"



# book1 = Book("The Hobbit", "Tolkien", 310)
# book2 = Book("Harry Porter", "Rowling", 223)
# book3 = Book("The Lion", "Lewis", 172)

# print(book1)
# print(book1 == book2)


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self.width:.1f}cm"
    
    @property
    def height(self):
        return f"{self.height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")


    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted successfully")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted successfully")
    

rectangle = Rectangle(3,4)
rectangle.width = 5
rectangle.height = 6

# del rectangle.width
# del rectangle.height

# print(rectangle._width)
# print(rectangle._height)

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("** You add sprinkles 🍨")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("added fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice-cream 🍨")

get_ice_cream("vanilla")







