def ui(retype = 'success'):
    if(retype == 'success'):
        print("Welcome to our STUDENT_SYSTEM")
    print("_____________________________")
    print("please sellect your user type")
    print("    1.Old user  0.New user   ")
    userType = int(input("Your Tpye: "))
    return userType;
def New_user(retype = 'success'):
    if(retype == 'success'):
        print("please input your username:")
        usr = input()
    print("please input your password")
    pwd_1 = input()
    print("please input your password again")
    pwd_2 = input()
    if(pwd_1 == pwd_2):
        #两次密码输入一致，创建用户
        global user
        newuser = {"%s"% (usr):"%s"%(pwd_1)}
        user.update(newuser)
        return 1
    else:
        #两次密码输入不一致，重新执行此函数
        print("两次密码输入不一致，请重新输入：")
        New_user('error')
    return 0
def Old_user():
    #Login
    print("＿＿＿＿Login Window＿＿＿＿")
    print("please input your username:")
    return 0
def main():
    userType = ui()
    while(userType != 1 and userType != 0):
        print("error! please input \"1\"or\"0\" ")
        userType = ui('error')
    #如果选择0，创建用户
    if(userType == 0):
        New_user()
    #新用户创建完成后，或者选择老用户时，进入登陆步骤
    Old_user()    

        
user={}     
main()
print(user)

