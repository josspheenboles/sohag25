#html
#selnumim,soup,request
import  re
pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email=input('enter email')
print(re.match(pattern,email))
print(re.fullmatch(pattern,email))
print(re.search(pattern,email))
print(re.findall(pattern,email))

# import  math
# print(math.pi)
# import os
# # path='/var/www1'
# # print(os.path.exists(path))
# #
# # open('/bin/python/','a')
# raise  Exception('my excep')
# import  sys
# print(sys.argv)
# print('name:',sys.argv[3])

# # n1=eval(input('enter number1 '))
# # n2=eval(input('enter number2 '))
# # print(n1+n2)
#
#
# modes=('r','w','a','r+')
# #read
# def read(filepath,option='all'):
#     file=open(filepath,modes[0])
#     if option=='all':
#         content=file.read()
#     elif isinstance(option,int):
#         content=file.read(option)
#     elif option=='line':
#         content = file.readline()
#     elif option=='lines':
#         content = file.readlines()
#     else:
#         content='invaid option'
#     file.close()
#     return content
# #write
# def  write(path,content):
#     pass
# #append
# #bounce convert as module
# c=read('asd.txt')
# print(c)
# import sys
# try:
#     1/0
#     int('1')
#     # read('sss')
# except ZeroDivisionError:
#     print('cann divi by zero')
# except ValueError:
#     print('cann cast to int')
# except:
#     print(sys.exc_info()[1])
# else:
#     print('else')
# finally:
#     print('finally')
#
#
# # #files
# # #open file
# # file=open('asd.txt','r')
# # #check is reaadable
# # if(file.readable()):
# #     for line in file:
# #         print(line)
# #     # #read
# #     # line=file.readline()
# #     # print(line)
# #     # line=file.readline()
# #     # print(line)
# #     # line=file.readline()
# #     # print(line)
# #     # line=file.readline()
# #     # print(line)
# #     # lines=file.readlines()
# #     # print(lines)
# #     # lines = file.readlines()
# #     # print(lines)
# #     # content=file.read(3)
# #     # print(content,type(content))
# #     # content = file.read()
# #     # print(content, type(content))
# #     # content = file.read()
# #     # print('==',content,'==',sep='')
# #
# # #close
# # file.close()
# # # #r--->file must be exsist,
# # # #w--->file will create
# # # filestream=open('asd.txt','a')#char0
# # # # print(type(filestream),filestream)
# # # if(filestream.writable()):
# # #     filestream.seek(7)
# # #     filestream.write('aya ali,python,sohag\n')
# # #     filestream.write('ahmed ali,iot,sohag\n')
# # #     listname=['mark','mai','sara','nada']
# # #     filestream.writelines(listname)
# # # if(filestream.readable()):
# # #     print(filestream.read())
# # # # # for name in listname:
# # # # #     filestream.write(name)
# # # filestream.close()
# # # #exception
# # # #modules
# # # # x=int('1')#cast from str to int
# # # # x=list(1,2,3,4)#cast from tuple to list
# # # # x,*y=6,'f',6,7,8,0
# # # # print(x,y)
# # # # #scope
# # # # #global scope -->have 0 indentation
# # # # # define var in script --->block level 1
# # # # intake='intake45'
# # # # #functions
# # # # #define function inside function
# # # # def outerfun():
# # # #     intake='outer intake' #local var in outer
# # # #     def innerfun():
# # # #         #deal interp. used first local var intake & modified it
# # # #         # nonlocal intake
# # #         #deal interp. used global var intake & modified it
# # #         global  intake
# # #         # intake='inner intake' #local var in inner
# # #         print(intake)#??
# # #         intake='palpalp' #?
# # #     innerfun()
# # #     print(intake)
# # # outerfun()
# # # print(intake)
# # # for n in range(13):
# # #     print(n,end='')
# # # if(n==12):
# # #     month='dec'
# # # print(n,month)
# # #local scope
# #
# # #*
# # #decalre variable---->* is list
# # #decalre arg---->* is tuple
# # #decalre arg---->** is dict
# # #calling function pass dict put ** ---->unpacking as key=value
# # #calling function pass tuple put * ---->unpacking as value1,....value2
# # #black box --->arguments & output
# # #define function
# # # '{name}'.format(name='ali')
# # # def myformat(**kargs):
# # #     print(kargs)
# # #     # print(type(kargs),kargs)
# # #     for key,val in kargs.items():
# # #         print(key,val)
# # #
# # # # myformat(name='ali',id=100)#packing {'name':'ali','id':100}
# # # d={'name':'ali','id':100}
# # # # myformat(key=d)#{'key':{}}#packing
# # # # t=(1,2,3)
# # # myformat(**d) #unpacking --->packing
# # # myformat(name='ali',id=100)
# # # # # min(1,2,34,5,67,7)
# # # def mymin(*args):
# # #     print(args)
# # # t=1,2,3
# # # mymin(*t)#unpacking--->packing
# #
# #
# # # range(1,5,1)
# # # range(1,5)
# # # range(end=5)
# # #tuple args
# # # *x,y=(4,5,6,7,2,3)#unpacking
# # # def myrang(*args):
# # #     if(len(args)==3):
# # #         print(f'start:{args[0]} end:{args[1]} step:{args[2]}')
# # #     elif(len(args)==2):
# # #         print(f'start:{args[0]} end:{args[1]} step:1')
# # #     elif(len(args)==1):
# # #         print(f'start:0 end:{args[0]} step:1')
# # # myrang(1,13,1)#(1,13,1)--->len--->3
# # # myrang(1,13)
# # # myrang(13)#(13,)--->len===>1
# # #
# # # # print(x)
# # # # def mysum(*args):#args is tuple
# # # #     # print(type(args),args)
# # # #     res=0
# # # #     for number in args:
# # # #         res+=number
# # # #     print(number)
# # # # t=1,2,3,4,5,6,'onrtf'
# # # # # mysum(t) #during calling --->packing (t,)
# # # mysum(1,2,3,4,5,6)#--->(1,2,3,4,5,6,....)
# # # #default arg-->intail value
# # # #non defaut arg then default
# # # def mysum(x=1,y=2,z=3):
# # #     print(x,y,z)
# # # mysum(5)
# # # mysum(1)#1-->in x
# # # mysum(10,20)#10--->x,20--->y
# # # mysum(10,20,30)
# # #keyword funame (arg1,arg2....)
# # # def mysum(arg1,arg2):
# # #    print(arg1+arg2)
# # # # #calling
# # # num1=eval(input('enter num1'))
# # # num2=eval(input('enter num2'))
# # # mysum(num1,num2)
# # # # print('====')
# # # mysum(1,2)
# # #read db & text file,excel
# # # var=5
# # # # txt=type(var)
# # # print(type(var))