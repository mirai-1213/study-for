#ui界面
def ui(retype = 'success'):
    if(retype == 'success'):
        print("Welcome to our STUDENT_SYSTEM")
    print("_____________________________")
    print("please sellect your user type")
    print("    1.Old user  0.New user   ")
    userType = input("Your Tpye: ")
    return userType;
#管理员ui界面
def admin_ui():
	print("***************************************")
	print("	1.All_user	2.Del_User		")
	print("		0.EXIT			")
	print("***************************************")
	doType = input("You want to do:")
	return doType
#创建新用户
def New_user(retype = 'success'):
	#global user
	if(retype == 'success'):
		print("please input your username:")
		usr = input()
		#检查是否存在重复的用户名，即在字典中进行key的遍历，重复返回0
		if(usrname_repeat(usr)==0):
			print("用户名重复，请输入新的用户名：")
			New_user()
			return 1#如果不需要递归，必须在之后return结束递归调用
	print("please input your password")
	pwd_1 = input()
	print("please input your password again")
	pwd_2 = input()
	if(pwd_1 == pwd_2):
		#两次密码输入一致，创建用户
		newuser = {"%s"%(usr):"%s"%(pwd_1)}
		user.update(newuser)
		return 1
	else:
		#两次密码输入不一致，重新执行此函数
		print("两次密码输入不一致，请重新输入：")
		New_user('error')
	return 0
#检查是否存在重复的用户名，即在字典中进行key的遍历，重复返回0
def usrname_repeat(usr):
	global user
	if(user.get(usr)!=None):
		return 0
	return 1
#登录
def Old_user():	#返回值是1登录成功 0登录失败
    #Login
	print("＿＿＿＿Login Page＿＿＿＿")
	print("please input your username:")
	usr = input()	
	print("please input your password")
	pwd = input()
	check_value = check(usr,pwd)#用户名，密码信息比对
	if(check_value==1):
		print("Login success")
		return 1
	elif(check_value==9):
		print("Enter in the Administrator Mode!")
		operation = Usr_operation()
		while(operation!=1):
			operation = Usr_operation()
	else:
		print("The username or password is incorrect. Please try again.")
		Old_user()
	return 0
#管理员用户信息验证
def Usr_admin(retype = 'success'):#管理员账户密码预设，usr=admin，pwd=admin
	global user
	if(retype == 'success'):
		pwd = input("Please enter the administrator password:\n")
	else:
		pwd = input("Please try again:\n")
	if(check('admin',pwd)==9):
		print("Enter in the Administrator Mode!")
		operation = Usr_operation()
		while(operation!=1):
			operation = Usr_operation()
	else:
		print("Failed!")
		Usr_admin("error")
	return 0
#管理员用户操作
def Usr_operation():
	doType = admin_ui()
	if(doType == '0'):
		return 1
	elif(doType == '1'):
	#预留管理员功能，可以查看全部用户数据
		All_user()
		return 0
	elif(doType == '2'):
	#预留管理员功能，可以删除指定用户数据
		All_user()
		user_del = input("请输入想要删除的用户的用户名：")
		if(user_del == "admin"):
			print("\nuser_admin is administrator,cannot delete!\n")
		else:
			user.pop(user_del)
			print("剩下的用户列表：")
			All_user()
		return 0
#显示全部用户信息
def All_user():
	for userItem in user.items():
		print(userItem)
	print()
#用户名密码验证
def check(usr,pwd):#正确返回1，不正确返回0，管理员返回9，异常返回-1
	global user
	#用户名不存在
	if(user.get(usr)==None):
		print("用户名不存在")
		return 0
	#密码不正确
	elif(user.get(usr)!=pwd):
		print("密码不正确")
		return 0
	else:
		if(usr=="admin"):
			return 9
		else:
			return 1
	print("密码验证时出现不明错误，请debug！")
	return -1
#主进程
def main():#手动退出返回1，其他情况退出返回0
	userType = ui()	#返回用户类型，新用户是1，老用户是0
	while(userType != '1' and userType != '0'):	#当既不是新用户又不是老用户时，执行循环，直到输入正确的数字
	#预留管理员账户功能  userType='admin'
		if(userType == 'admin'):
			Usr_admin()
			return 1
		else:
			print("error! please input \"1\"or\"0\" ")
			userType = ui('error')	#传入“error”，实际上传入任意非“success”值都可以
	if(userType == '0'):    #如果选择0，创建用户
		New_user()
	#新用户创建完成后，或者选择老用户时，进入登陆步骤
	if(Old_user()==1):
		#预留主模块接口
		#退出登录 目前无论输入什么都退出登录
		if(input("If you want to quit the login, please input \"exit\"")=="exit"):
			return 1
		else:
			return 0
	
#begin-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
user={"admin":"admin"}	#创建一个只有管理员用户信息的字典
#加入文件操作后，讲用户信息写入独立文件
while(1):
	main()
	#输入“exit”退出程序，输入其他任意值从头再次执行程序
	if(input("If you want to quit the program, please input \"exit\"\n Enter any letters to return to the login page\n")=="exit"):
		break;
	else:
		continue

