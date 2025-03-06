# from Day5.magical import humanobj
# def mysum(x,y):
#     pass
# def mysum(x,y,z):
#     pass

class Human:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def speek(self):
        print(f'iam {self.name}')
class Employee(Human):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary
    def  speek(self):
        # super().speek()
        print(f'name:{self.name}')
humanobj=Human(1,'aya')
emp=Employee(2,'mark',8000)
# humanobj.speek()
emp.speek() #employee contatin def o