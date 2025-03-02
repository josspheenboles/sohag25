#module constatin only defination
#var,function,classes
modes=('r','w','a','r+')
# #read
def read(filepath,option='all'):
    # if(os.path.exists(path=filepath)):

        file=open(filepath,modes[0])
        if option=='all':
            content=file.read()
        elif isinstance(option,int):
            content=file.read(option)
        elif option=='line':
            content = file.readline()
        elif option=='lines':
            content = file.readlines()
        else:
            content='invaid option'
        file.close()
        return content

    # else:
    #     return  'file not exsist'
# #write
def  write(path,content):
    pass
# #append
def append(path,content):
    pass