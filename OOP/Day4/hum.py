class Car:
    def __init__(self,color,model):
        self.color=color
        self.model=model
class Employee:
    def __init__(self,id,name,salary,position,objcar):
        self.id=id
        self.name=name
        self.salary=salary
        self.position=position
        self.mycar=objcar
    def getcarinfp(self):
        return self.mycar.color
    def drive(self,objcar):
        print(objcar.color)

objcar=Car('black','128')
empob=Employee(1,'aya',5000,'back',objcar)
empob2=Employee(1,'amrk',5000,'front','obj')
print(empob.getcarinfp())
# empob2.getcarinfp()


# class Human:
#     count=0
#     live=True
#     #pass obj add to self
#     def __init__(self,id,name='ahmed'):
#         self.id=id
#         self.name=name
#         Human.count+=1
#         print('object created')
#     #method realted class logic in same time  not ralted to instance
#     #static method
#     @staticmethod
#     def mesuretemp(temp):
#         if (temp < 37):
#             print('you have cld')
#         elif (temp > 37):
#             print('hot')
#         else:
#             print('normal')
#     #method ralated class
#
#     @classmethod
#     def getpopulation(cls):
#         print(cls.count)
#     #instance method
#     #its logic realted to instance
#     def eat(self):
#         print(f'iam eating {self.name}')
#     def drink(self,whatudrink):
#         print(f'iam {self.name} drink {whatudrink}')
#
#
# obj1=Human(1,'aya')#no constr?? contain 2 instance id,name
# Human.mesuretemp(23)
# obj1.mesuretemp(37)
#
#
# #
#
# # obj2=Human(2,'mai')#no constr??
# # obj1.getpopulation()
# # Human.getpopulation()
# # # obj1.eat()
# # # obj2.eat()
# # # obj2.drink('tea')
# # # obj1.drink('coffe')
# # # # obj1.gender='F'
# # # obj1.live=False
# # # # obj1.count=-1#conver count to instance var in obje1
# # # obj1.id=1#replace none with id
# # # obj1.name='aya'
# #
# # obj3=Human(3)
# # # obj2.id=2
# # # obj2.name='mai'
# # print(Human.live)
# # print(obj1.live)
# # print(obj2.live)
# # print(obj3.live)