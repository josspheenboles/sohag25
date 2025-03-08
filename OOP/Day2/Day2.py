l=eval(input('enter list of names'))

print(type(l))
# l=[]
# for number in range(1,13):
#     if number%2!=0:
#         l.append(number)
# print(l)
# # [value loop condation]
# #loop -->value pass condition -->true will append
# l2=[number for number in range(1,13) if number%2!=0]
# print(l2)
#
# # #(1,3,address)
# # t=(1,3,[])
# # # t[2]=[4]#creatbe obj of list
# # t[0]='plplpl'
# # t[2].append('d')
# # print(t[2])
# # print(t)
# # # l=['python']
# # l2=[]
# # # l2=l#shallow copy
# # l2=l.copy()
# # l[0]='Java'
# # print(l,l2)
# # # d={}
# # # print(d['id'])
# # # x=(5,)
# # # t=
# # # x,z,*y=5,6,7,8,9,10
# # # print(x,z,y)
# # # y[0]=1000
# # # t=5,6
# # # print(type(t))
# # # #varnam1,var2=tuple
# # # x,y=t#unpacking
# # # print(x,y)
# # # # name='aya ali'
# # # # for index,value in enumerate(name):#iteratable collectio of tuple
# # # #     print(index,value)
# # #
# # #
# # # # # l=[1,'asd']
# # # # # print(sort(l))
# # # # # #
# # # # # # # #functions
# # # # # # # #scope
# # # # # # # #exception handling
# # # # # #Data stucture
# # # # #dict ==>collection of pairs key:values ,diff data type,hetero
# # # # #key must be uniq
# # # d={
# # #     'id':1,
# # #     'name':'aya ali',
# # #     'gpa':3.9,
# # #     'courses':['python','java'],
# # #     'grades':(100,99),
# # #     'isgraduated':True,
# # #     # 'id':1000
# # #
# # # }
# # # for x in d.items():
# # #     print(x)
# # # # # d['cgrades']={'python':100,'java':99}
# # # # d1={'track':'python inten.','id':1000}
# # # # d.update(d1)
# # # #
# # # # # d['id']=200
# # # # # print(d+d1)
# # # # print(d)
# # # # print(d1)
# # # # # for item in d.items():
# # # # #     print(item)
# # # # #     key in d.keys():
# # # # #     print(key)
# # # # # for key in d:
# # # # #     print(key,':',d[key],type(d[key]))
# # # # # print(d['id'])
# # # # # print(type(d),d)
# # # # # # tuple--->collection of values ,diff data type,hetero,tuple is immutable
# # # # # t=(1.3,)
# # # # #
# # # # #
# # # # # # t[0]='one'
# # # # #
# # # # # # print(t[0],t[1:4],t[::-1])
# # # # # print(type(t),t)
# # # # # # s={'mai','ahmed',-1,4}
# # # # # # print(s)
# # # # # # l=['mai','ahmed']
# # # # # # l.sort()
# # # # # # l.reverse()
# # # # # # print(l)
# # # # # # admintech=[1,'bash','admin1','bash']
# # # # # # progtech=['python','js','django','flask']
# # # # # # # # print(admintech+progtech)
# # # # # # print(admintech.extend(progtech))
# # # # # # # admintech.append(progtech)
# # # # # # print(admintech)
# # # # # # print(progtech)
# # # # # # # print(len(admintech))
# # # # # # print(admintech)
# # # # # # # print('aya '+'ali')
# # # # # # # print(admintech*3)
# # # # # # # # name='aya ali'
# # # # # # # #immutable
# # # # # # # # name[0]='A'
# # # # # # # print(name.replace('a','A',1))
# # # # # # # name='A'+name[1:]
# # # # # # # print(name)
# # # # # # #list--->collection of values ,diff data type,hetero
# # # # # # mylist=[1,1.1,True,'asd',[3,4,'dfd'],(),{},'asd']
# # # # # # # for item in mylist:
# # # # # # #     if(item==True and isinstance(item,bool)):
# # # # # # #         print(item)
# # # # # # #         break
# # # # # # # mylist.append(range(1,14))
# # # # # # # mylist.insert(1,'plplpa')
# # # # # # # print(mylist.pop())
# # # # # # # print(mylist.pop(1))
# # # # # # # 1==True
# # # # # # print(mylist.remove(True))
# # # # # # print(mylist)
# # # # # # # # mylist[0]='one'
# # # # # # # # print(mylist[0])
# # # # # # # print(mylist[-1])
# # # # # # # # for item in enumerate(mylist):
# # # # # # #     print(item,type(item))
# # # # # # # print(type(mylist),mylist)
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # # # #control flow (if,for,while)
# # # # # # # #
# # # # # # # print(range(1,13))
# # # # # # # name='aya ali'
# # # # # # # print(enumerate(name))
# # # # # # # print(enumerate('aya ali'))
# # # # # # # # flag=True
# # # # # # # # while flag==True:
# # # # # # #     num=input('enter number')
# # # # # # #     answer=input('enter y for cont. no for other')
# # # # # # #     if(answer=='n' or answer=='N'):
# # # # # # #         flag=False
# # # # # # # # for num in range(1,5):
# # # # # # #     if(num==3):
# # # # # # #         continue
# # # # # # #     print(num)
# # # # # # # else:
# # # # # # #     print('all numbers printed')
# # # # # # # name='aya ali'
# # # # # # # for char in name:
# # # # # # #     if(char=='a'):
# # # # # # #          break
# # # # # # #     print(char,end='')
# # # # # # # #else run code reach last loop
# # # # # # # else:
# # # # # # #     print('===i reached for lastt loop===')
# # # # # #
# # # # # # # #for loop in any collection or itertable
# # # # # # # # #genertate numbers [start=0],end,[step=1]
# # # # # # # # range(0,13,1)#[0....12]
# # # # # # # # range(0,13)#[0....12]
# # # # # # # # r=range(13)#[0....12]
# # # # # # # # # DateTime--->self study
# # # # # # # # for number in range(13):
# # # # # # # #     print(number,'number as l')
# # # # # # # # print(r)
# # # # # # # name='aya ali'
# # # # # # # for char in name:
# # # # # # #     if(char=='l'):
# # # # # # #         continue
# # # # # # #     print(char,sep='',end=' ')
# # # # # # # else:
# # # # # # #     print('all loops done')
# # # # # # # # obj1=enumerate(name)
# # # # # # # # for item in obj1:
# # # # # # # #     print(item,f'Index : {item[0]},Char:{item[1]}')
# # # # # # # # print(obj1)
# # # # # # # # index=0
# # # # # # # # for char in name:
# # # # # # # #     print(char,index)
# # # # # # # #     index+=1
# # # # # # # # num1=10
# # # # # # # # if num1>5 and num1<11:
# # # # # # # #     print('in ranger')
# # # # # # # # num1=input('enter number')
# # # # # # # # if(num1=='0'):
# # # # # # # #     print('zero')
# # # # # # # # elif(num1=='1'):
# # # # # # # #     print('One')
# # # # # # # # else:
# # # # # # # #     print('invalid number')
# # # # # # # #
# # # # # # # # if(num1=='0'):
# # # # # # # #     print('Zero')
# # # # # # # # else:
# # # # # # # #     if(num1=='1'):
# # # # # # # #         print('One')
# # # # # # # #     else:
# # # # # # # #         print('invalid ')
# # # # # # # # # str --->isdigit ()
# # # # # # # # # num1=(input('enter number'))
# # # # # # # # #soluation
# # # # # # # # # if(num1.isdigit() or num1.isdecimal()):
# # # # # # # # #     num1=float(num1)
# # # # # # # # # else:
# # # # # # # # #     print('error')
# # # # # # # # #soluation
# # # # # # # # # num1=eval(input('enter num'))
# # # # # # # # # print(type(num1))