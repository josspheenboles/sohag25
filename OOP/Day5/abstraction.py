from abc import  ABC,abstractmethod
class Human(ABC):
    def test(self):
        print('test')
    @abstractmethod
    def eat (self):
        pass
    @abstractmethod
    def walk(self):
        pass
#inhertance from abstract class withour override to it abstract method
class Test(Human):
   def walk(self):
       pass
   def eat(self):
       pass
   def fun(self):
        print('iam fun')
t=Test()
# h=Human()
# h.walk()
# #abstract
# #standred module
# from abc import ABC, abstractmethod
# #inhrite from ABc --->human abstract class
# class Human(ABC):
#     def __init__(self):
#         self.id=None
#     @abstractmethod
#     def walk(self):
#         pass
# class Sol(Human):
#
#     def walk(self):
#         print('iam sold. walking')
# # h=Human()
# # h.walk()
# s=Sol()
# s.walk()