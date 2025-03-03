class Human:
    count=0
    # live=True
    #constructor
    #called autom. when object created
    #ref to object will be created
    def __init__(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender
        Human.count += 1
        print(f'iam human constr. {self}')
obj1=Human(1,'aya','F')

