def writeInFile(user,writeType='w'):#字典写入文件
    if(writeType == 'a'):
        fp = open("usrinfo",'a+')
        fp.write(str(user))
        fp.close()
        return 1
    fp = open("usrinfo",'w+')
    fp.write(str(user))
    fp.close()
    return 1
    
def loadFromFile():#从文件中读取字典,返回一个字典对象
    global user
    try:
        fp = open("usrinfo",'r+')
        if(user.get("admin",'a')==None):
            user.update({"admin":"admin"})
            writeInFile(user)
    except:
        user.update({"admin":"admin"})
        writeInFile(user)
        loadFromFile()
        return user
    user = eval(fp.read())
    fp.close()
    return user

user = {}
