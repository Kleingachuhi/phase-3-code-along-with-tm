# CLASS 
#  classes are blueprints.



from os import name


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
print(my_box.area())



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
print(p1.name)
