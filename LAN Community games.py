'''4 main tabs are as follows-Games near me, Communities, Friends and Profile '''
userlist=[]
class mail():
    def __init__(self,notification,sender,content=' '):
        self.notification=notification
        self.content=content
        self.sender=sender
    def __str__(self):
        return 'Its mail...'
    def displayMail(self):
        print("contents")
        print(f"from {sender}")
    def friendRequest(self):
        print('You have recieved a friend requeset from {}'.format(self.sender))
        accept=input("would you like to accept: ")
        test=True
        while test:
            if accept=='yes':
                self.friends.append(sender)
                sender.friends.append(self.username)
                test=False
            elif accept=='no':
                denied=mail('mail',self.username,'Your request has been denied')
                sender.mailbox.append(denied)
                test=False
            else:
                accept=input("Yes or No: ")
    def checkMail(self):
        for x in self.mailbox:
            if self.notification=='mailing':
                displayMail()
            elif self.notification='friendRequest':
                friendRequest()
            else:
                pass
class user():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.community=None
        self.friends=[]
        self.mailbox=[]
        self.special=None
    def __str__(self):
        return "Username is {}".format(self.username)
    def addFriend(self):
        friend=input("Who would you like to add?")
        found=False
        while found==False:
            for x in userlist:
                if friend==x.username:
                    self.friends.append(x)
                    found=True
                else:
                    pass
            if found==False:
                print("that person was not found")
                friend=input("try again?")
                if friend=='yes':
                    friend=input("Username: ")
                elif friend=='no':
                    found=True
                else:
                    print('please enter yes or no')
                    friend=input(': ')
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
        test=False
admin=user('atbauchat','Bauchat1')
userlist.append(admin)
createNewUser()
for x in userlist:
    print(x)
userlist[0].addFriend()
