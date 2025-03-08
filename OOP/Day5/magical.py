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
    #magical method autocalling
    #__str__ return str
    def __str__(self):
        return f'ID:{str(self._id)},Name:{self.name},Gender:{self.__gender}'
    def __len__(self):
        return len(self.name)

humanobj=Human(1,'aya ali','F')
print(len(humanobj))#human ?? __len__ --->no Obect__len__