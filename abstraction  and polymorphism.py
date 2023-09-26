# abc
"""
Abstract classes
- They provide a specific convection of crating subclasses
- They cannot be instantied , meaning we cannot create an object of an abstracct class
- Abstract classes hold empty methods (known as abstract methods), which helps guide on which subclass should have.
What is a subclass?
-A subclass is a class that implements an abstract class.This means that it has to adhere to abstract classes methods i.e: it must implement the empty methods defined in the abstract class. i.e Different subclasses implement the abstrsct methods in different ways.

Example: We can have the class 2D shapes(i.e:shapes such as Square, Rectangles, Circles, Triangle e.t.c) thisabstract class will contain the methods that should be implemented for any 2D shape, in common, for example they should all have
an area and a perimeter. In this abstract class we will have empty abstract methods area and perimeter which can be implemented by subclasses of the abstract class e.g  Square or Circle where based on this  
them having their own implementation of perimeter and area.

In python wee use the module 'abc' that stands for abstract base classes, to implement abstraction.It  has the following important classes and methods:
1. ABC - This is the base class that contains all abstract class characteristics
2. ABCMeta - This is the meta class used to ensure that the abstract class adheres to an abstract classes characteristics.
3. Abstractmethod- This is placed as a decorator on top of all methods inside an abstract method to tag them as abstract methods.

Whats a decorator?
A decorator is a special function, usually called by using the symbol'@' befoore the function name , it does not include '()' at the end, and it is placed above another function name, it doesn't include '()' at the end and it is
placed above another function, so as to add a particular chareacteristic/ functionality just before or aafter a function is called.In case the @abstractmethod is placed on method inside an abstract class, where it makes the method to have the characteristics of an abstract method.
NB: A decorator takes in another function as its parameter
"""

from abc import ABC, ABCMeta, abstractmethod

#2D shapes
class Shapes(ABC, metaclass=ABCMeta):
    #TODO Research on keyword arguements in pyhton also usage of **kwargs
    @abstractmethod
    def perimeter(*args):
        pass

    @abstractmethod
    def area(self, *args):
        pass

class Rectangle(Shapes):
    def __init__(self, shape_name):
        self.shape = shape_name

    def perimeter(self, width, height):
        return 2*(width+height)
    
    def area(self, 
             width, height):
        return width*height
    
    def print_shape(self):
        print(self.shape)

rectangle = Rectangle("Rectangle")
rect_perimeter = rectangle.perimeter(10,30)
rect_area = rectangle.area(10,30)

rectangle.print_shape()
print(f"AREA: {rect_area}")
print(f"PERIMETER: {rect_perimeter}")