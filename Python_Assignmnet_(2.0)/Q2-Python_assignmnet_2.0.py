"""
2. Define a class Person and its two child classes: Male and Female. All classes have
a method "get_gender" which can print "Male" for Male class and "Female" for Female
Class.
Bonus: Make class Person an abstract class and make get_gender an abstract method in the
same class. The two child classes must inherit and implement get_gender. i.e., When trying to
initialize an object of class Person, the program must throw an error
"""

from abc import ABC,abstractmethod
class Person(ABC):
    @abstractmethod
    def get_gender(self):
        pass
class Male(Person):
    def get_gender(self):
        print("Male")
class Female(Person):
    def get_gender(self):
        print("Female")
per=Person()
#per.get_gender()  
"""Traceback (most recent call last):
  File "C:\Users\Admin\Desktop\Practice&assignmnet foler\Assignmnet_questions_solution\Python_assignmnets\Q2-Python_assignmnet_2.0.py", line 20, in <module>
    per=Person()
        ^^^^^^^^
TypeError: Can't instantiate abstract class Person without an implementation for abstract method 'get_gender'
"""
male=Male()
male.get_gender()
female=Female()
female.get_gender()