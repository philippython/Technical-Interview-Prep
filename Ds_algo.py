from datetime import datetime
# Python program to demonstrate
# use of class method and static method.
from datetime import date
 
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
class Robot(Person):
    def __init__(self, name, age, model, function_):
      super().__init__(name, age)
      self.model = model
      self.function_ = function_
    
    @classmethod
    def fromBuildDate(cls, name, year, model, function_):
      return cls(name, datetime.now().year - year, model, function_)

bot = Robot("roblox", 1, "BOT#($", "space engine")
botx = Robot.fromBuildDate("robloxt", 2009, "BOTX", "humroid")
print(botx.function_)
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(22))

# MRO method resolution method

# used in inheritance 
# it's the order in which a method is serached in a classes inheritance

class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

d = D()
d.method()

