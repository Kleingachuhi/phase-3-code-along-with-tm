# CLASS 
#  classes are blueprints.





class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says woof!"
    def sleep(self):
        return f"{self.name} has fallen asleep!"
dog1 = Dog("Bosko", 3)
dog2 = Dog("Liam", 5)
# print(dog1.bark())
# print(dog2.bark())
# print(dog1.sleep())

#INHERITANCE AND SUPER()
# the super acts as a connector between the parent and child class.
class Parentclass:
    def __init__(self, param):
        self.param = param
class Childclass(Parentclass):
    def __init__(self, param, extra_param):
        super().__init__(param) # --> this is the syntax of the parent subclass connection and super is what inherits the parameters from the parent class
        self.extra_param = extra_param

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound!"
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def speak(self):
        return f"{self.name} meows!"
cat1 = Cat("Whiskers", "Brown")
# print(cat1.speak())
# print(cat1.color)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start_engine(self):
        return f"{self.brand} engine started!"
class Motorcycle(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type
    def wheelie(self):
        return f"{self.brand} {self.type} does a wheelie!"
bike1 = Motorcycle("Yamaha", "sport")
# print(bike1.start_engine()) # --> here we see a child class can get from tbe parent as it is calling from the parent class.
# print(bike1.wheelie())

class Shape:
    def __init__(self):
        pass
    def area(self):
        return "Area not defined"
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
my_box = Rectangle(40, 20)
# print(my_box.area())



#  CLASS ATTRIBUTES
class School:
    location = "Ngong road" # --> it is passed to the entire class.
    def __init__(self, name):
        self.name = name
    def info(self):
        if self.name == "Moringa School":
            self.location = "Ngong road"
        elif self.name == "Strathmore University":
            self.location = "Madaraka Estate"
        return f"{self.name} is located along {self.location}."
school1 = School("Moringa School")
school2 = School("Strathmore University")
# print(school1.info())
# print(school2.info())

#CLASS METHODS
# These are methods that operate on the class itself and not instances. They have the @classmethod decorator and they take a cls attribute.
class Classname:
    @classmethod
    def class_method_name(cls, param):
        #write your code here
        return f"Class method called with {param}"
    
class Person:
    def __init__(self, name):
        self.name = name
    @classmethod
    def from_string(cls, string):
        name = string.split(",")[0]
        return cls(name)
p1 = Person.from_string("Alice, 23")
# print(p1.name)


# CLASS ATTRIBUTES TOGETHER WITH CLASS METHODS
class Book:
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books +=1 # if you want to keep track of data once updated like keeping count, its best to use the += 1 in the init since ince it is initialized you get to note the increment
    @classmethod
    def get_total_books(cls):
        return cls.total_books
my_book1 = Book("Harry Potter", "J.K Rowling")
my_book2 = Book("The Hobbit", "J.R.R. Tolkien")
my_book3 = Book("1984", "George Orwell")
print(Book.get_total_books())

#MANY TO MANY RELATIONSHIP
# --> This is a relationship where multiple objects of on class can be associated with many objects of another class

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll_course(self)
    def list_students(self):
        return [student.name for student in self.students]
    def __str__(self):
        return self.name
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
    def list_courses(self):
        return [str(course) for course in self.courses]

student1 = Student("Klein")
student2 = Student("Peter")
course1 = Course("Algebra")
course2 = Course("Python")

course1.enroll_student(student1)
course1.enroll_student(student2)
course2.enroll_student(student2)
print(course1.list_students())
print(course2.list_students())
print(student2.list_courses())

class Book:
    def __init__(self, title):
        self.name = title
        self.book_shelf = []
    def enroll_book(self, book):
        if book not in self.book_shelf:
            self.book_shelf.append(book)
    def list_books(self):
        return [book.title for book in self.book_shelf]
    def __str__(self):
        return self.book_shelf
class Author:
    def __init__(self, name):
        self.name = name
        self.author_collection = []
    def enroll_author(self, author):
        if author not in self.author_collection:
            self.author_collection.append(author)
    def list_authors(self):
        return [author.name for author in self.author_collection]
    
book1 = Book("Harry Potter")
book2 = Book("The Hobbit")
author1 = Author("J.K. Rowling")
author2 = Author("Someone")
book1.enroll_book(author1)
book1.enroll_book(author2)
author1.enroll_author(book1)
author1.enroll_author(book2)
print(author1.list_authors())
print(str(book1.book_shelf))