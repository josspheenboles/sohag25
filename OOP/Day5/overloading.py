from multipledispatch import dispatch
from OOP.Day5.multilevel import Human
@dispatch(int, int)
def mysum(x,y):
    (print(x+y)
@dispatch(float, float))
def mysum(x,y):
    print(x+y)
@dispatch(Human, Human)
def mysum(x,y):
    print(x.id+y.id)
mysum(1,2)
mysum(1.2,1.1)
# def mysum(datatype,*values):
#     res=0
#     if(datatype=='int' or datatype=='str'):
#         for val in values:
#             res+=val
#     elif(datatype=='Human'):
#         for obj in values:
#             res+=obj.id
# mysum('int',1,2,3,4)
# # from magical import Human
# # def mysum(x,y):
# #     print(x+y)
# # mysum(1,2)
# # mysum('aya' ,'ali')
# # mysum(1.2,2.2)
# # mysum([1,2],[3,4])
# # mysum(Human(1,'aya','G'),Human(1,'mai','k'))
# # # def mysum(*args):
# # #     print(args)
# # # mysum(1,2,3)
# # # mysum(1,2,3,4,45)
# # # def mysum(x,y,z=0):
# # #     print(x,y,z)
# # # mysum(1,2)
# # # mysum(1,2,3)
# # # #function if first class citizen
# # # #funactio as var
# # # def mysum(x,y):
# # #     print(x,y)
# # # print(mysum,mysum(1,2))
# # # def mysum(x,y,z):
# # #     print(x,y,z)
# # # # mysum(1,2)
# # # # mysum(1,2,3)
# # # print(mysum,mysum(1,2,3))