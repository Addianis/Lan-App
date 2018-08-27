'''4 main tabs are as follows-Games near me, Communities, Friends and Profile '''
userlist=[]
def send(message):
    found=False
    for x in userlist:
        if message.target==x.username:
            x.mailbox.append(message)
            found=True
            print('message sent')
        else:
            pass
    if found==False:
        print("user not found")
class mail():
    def __init__(self,notification,sender,target,content=' '):
        self.notification=notification
        self.content=content
        self.sender=sender
        self.target=target
    def __str__(self):
        return 'Message from {}'.format(self.sender)
    def displayMail(self):
        print("contents")
        print(f"from {sender}")
    def friendRequest(self,user):
        print('you have recieved a friend request from {}'.format(self.sender))
        answer=("Would you like to accept: ")
        test=False
        while test==False:
            if answer=='yes':
                user.friends.append(self.sender.username)
                self.sender.friends.append(user.username)
                print(f"{user.username} has become friends with {self.sender.username}")
                test=True
            elif answer=='no':
                print("You have not accepted the request.")
                test=True
            else:
                answer=input("yes or no: ")
    def checkMail(self,user):
        if self.notification=='friendRequest':
            self.friendRequest(user)
        else:
            print("NOT IMPLEMENTED!")
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
                    print("Would you like to send a message?")
                    yes=input('Yes or No: ')
                    if yes=='yes':
                        message=input("message: ")
                    else:
                        message=' '
                    possibleFriend=mail('friendRequest',self,friend,message)
                    send(possibleFriend)
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
for x in userlist[1].mailbox:
    x.checkMail(userlist[1])
print(userlist[0].friends)
