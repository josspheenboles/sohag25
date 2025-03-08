class Human:
    count=0
    def __init__(self,id,name,gender):
        #protected
        self._id=id
        self.name=name
        #call setter
        self.setgender(gender)
        Human.count+=1
    def eat(self):
        print('Human iam eated')
    def walk(self):
        print('Human walked')
    def setgender(self,newgender):
        # private
        if (newgender == 'F' or newgender == 'M'):
            self.__gender = newgender
        else:
            self.__gender = 'F'
    def getgender(self):
        return self.__gender

    # function changer behivar instance method
    #self.instancemethosname()--->self.instacnemethod
    @property
    def Gender(self):
        return self.__gender

    # self.instancemethosname(newvalue)--->self.instacnemethod=newvalue
    @Gender.setter
    def Gender(self,newvalue):
        if newvalue in ('F','M'):
            self.__gender=newvalue
        else:
            self.__gender='F'

class Employee(Human):
    def __init__(self,id,name,gender,salary,position):
        super().__init__(id,name,gender)
        self.salary=salary
        self.position=position
human =Human(1,'zz','plapla')
# # human.gender='k'
# human.setgender('M')
# human.Gender='ddd'
# print(human.getgender(),human.Gender)
# # human._id=100
# print(human._id)
# print(human.__gender)
# empobj=Employee(1,'aya','palpalp',8000,'backe')
# #access obj
# print(empobj.__gender)
# class Doctor(Employee):
#     pass
# d=Doctor(1,'aya','F')
# # empobj=Employee(1,'aya ','F',8000,'back end j.')
# # print(empobj.id,empobj.name,empobj.salary)
# empobj.walk()
# # #boxing
# # objhuman=Human(1,'aya ali','F')
# #unboxing
# print(objhuman.id)
# # print(Human.count)
# # #boxing  obj of employee---> obj of human
# objemp=Employee(1,'mostafa','M')
# print(objemp,objemp.id)#unboxing