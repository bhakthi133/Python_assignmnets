"""

Topic: OOP: Classes, __init__, Inheritance & Polymorphism 

Build a class hierarchy for a library system: 

(a) Base class LibraryItem: title, author, year, describe() method. 
(b) Subclass Book: add pages and genre, override describe(). 
(c) Subclass Magazine: add issue_number and is_monthly, override describe(). 
(d) Create a list with one Book and one Magazine, loop and call describe() -- demonstrate polymorphism. 
(e) Predict the output: class Animal:     def __init__(self, name): self.name = name     def speak(self): return f'{self.name} speaks' class Dog(Animal):     def speak(self): return f'{self.name} says Woof!' for a in [Animal('Cat'), Dog('Rex')]:     print(a.speak()) 

"""

class LibraryItem:
    def __init__(self,title, author, year):
        self.title=title
        self.author=author
        self.year=year
    def describe(self):
        print("Library item class")
        print(f"The {self.title} written by {self.author} in {self.year}")

class Book(LibraryItem):
    def __init__(self,title,author,year,pages,genre):
        super().__init__(title,author,year)
        self.pages=pages
        self.genre=genre
    def describe(self):
        print("The book class")
        print(f"The {self.title} written by {self.author} in {self.year}and have {self.pages} pages & it's genre is {self.genre}")

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_no, is_monthly):
        super().__init__(title, author, year)
        self.issue_no=issue_no
        self.is_monthly=is_monthly
    def describe(self):
        print("The magazine class")
        print(f"The {self.title} written by {self.author} in {self.year}and with issue {self.issue_no} of monthly {self.is_monthly}")
        

library=LibraryItem("Nakuthanthi","Dara Bendre",1960)
#library.describe()
books=Book("Nakuthanthi","Dara Bendre",1960,100,"Kannada poetry")
#books.describe()
magazines=Magazine("Nakuthanthi","Dara Bendre",1960,1234,"Yes")
#magazines.describe()
l=[library,books,magazines]
for i in l:
    i.describe()
    print("==========================================================================")
