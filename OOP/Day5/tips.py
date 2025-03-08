class Person:
    moods=('Happy','Lazy','Trired')
    def __init__(self):
        self.__moode=Person.moods[0]
    def sleep(self,hours):
        if(hours>7):
            self.__moode=Person.moods[1]


# iseven=lambda n:n%2==0
# l=[1,2,3,4,5,6,7,8]
# it=filter(iseven,l)
# for x in it:
#     print(x)
# # evnum=[]
# # for n in l:
# #     if iseven(n):
# #         evnum.append(n)
# # print(evnum)
# # # inc=lambda x:x+1
# # l=[1,2]
# # l=map(lambda x:x+1,l)
# #
# # # for index,val in enumerate(l):
# # #     l[index]=inc(val)
# # # print(l)
# #
# # # def fun():
# # #     for n in range(3):
# # #         yield  n#packing number in generator object
# # #
# # # # def fun (number):
# # # #     for n in range(number): #[0,,,,number]
# # # #         return n#rerutn 0 desctroy
# # # var=fun()#srart,end,step
# # # print(var,type(var))
# # # print(next(var))
# # # # print(next(var))
# # # # print(next(var))
# # # l=[0,1,2]#
# # # it=iter(l)#store 0...2 in memory
# # # print(next(l))
# # # print(next(l))
# # # print(next(l))
# # #
# # # # print(next(var))
# # # # # r=range(1,100000000)
# # # # # l=[1,2]
# # # # # print(l[0])
# # # # i=iter({1,2,3,4,6})#index0
# # # # print(next(i))#index0--->index=1
# # # # print(next(i))
# # # # print(next(i))
# # # # print(next(i))
# # #
# # # # for c in r:
# # # #     print(c)
# # # # for c in []:
# # # #     print(c)
# # # # r=range(1,13)
# # # # itr=iter(r)
# # # # print(next(itr))
# # # # # l=['aya','ali']
# # # # # it=iter(l)
# # # # # print(next(it))
# # # # # print(next(it))
# # # # # print(next(it))
# # # # # def mysum(y):
# # # # #     var=lambda x:x+y
# # # # #     return var
# # # # #
# # # # # print(mysum(3)(4))#y===>3 x===>4
# # # # # # #lamda expresioin
# # # # # # #define anoynomous func & its body one line
# # # # # # # lambda inputs:output
# # # # # # varname=lambda x: x+1
# # # # # # print(varname(7))
# # # # # # varname='asd' #object of str
# # # # # # # if(varname.iscallable()):
# # # # # # print(varname(3))
# # # # # #
# # # # # # # with open('nots','r') as f:
# # # # # # #     print(f.read())
# # # # # # #     print('-------')
# # # # # # #     f.clos()
# # # # # # # print('====')