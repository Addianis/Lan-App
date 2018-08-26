'''4 main tabs are as follows-Games near me, Communities, Friends and Profile '''
userlist=[]
class user():
	def __init__(self,username,password):
		self.username=username
		self.password=password
		self.community=None
		self.friends=[]
	def __str__(self):
		return "Username is {}".format(self.username)
def createNewUser():
	test=True
	while test:
		name=input('Username: ')
		for x in userlist:
			if x.username==name:
				print("That name is taken, please choose a different one/n")
				name=input("Username: ")
			else:
				test=False
	print('Now please pick a password')
	password=input("password: ")
	password2=input("please reenter your password: ")
	while password!=password2:
		print("those didn't match. Would you like to try a new password or reenter the old one?")
		option=input("new password or reenter: ")
		if option=='new password':
			password=input("password: ")
			password2=input("Please reenter the password: ")
		elif option=='reenter':
			password2=input("Password: ")
	test=user(name,password)
	userlist.append(test)
admin=user('atbauchat','Bauchat1')
userlist.append(admin)
createNewUser()
createNewUser()
for x in userlist:
	print(x)