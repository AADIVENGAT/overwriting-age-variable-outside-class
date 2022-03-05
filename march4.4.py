#overwriting age variable outside class
class Person:
    def __init__(self,name,age): #__init__ = constructor,magic method
       self.name = name      #self = current object #name = object variable
       self.age = age
    def greet(self):
        print("Hello " + self.name)

p1 = Person("AADITYA",20)
p1.age = 21
print(p1.age)