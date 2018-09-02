'''4 main tabs are as follows-Games near me, Communities, Friends and Profile '''
class mainManager():
    def __init__(self):
        self.userList=[]
        self.communityList=[]
    def createNewUser(self):
        test = True
        while test:
            name = input('Username: ')
            for x in self.userList:
                if x.username == name:
                    print("That name is taken, please choose a different one/n")
                    name = input("Username: ")
                else:
                    test = False
            print('Now please pick a password')
            password = input("password: ")
            password2 = input("please reenter your password: ")
            while password != password2:
                print("those didn't match. Would you like to try a new password or reenter the old one?")
                option = input("new password or reenter: ")
                if option == 'new password':
                    password = input("password: ")
                    password2 = input("Please reenter the password: ")
                elif option == 'reenter':
                    password2 = input("Password: ")
            account = user(name, password)
            test = False
        self.userList.append(account)
    def send(self,message):
        # Sends a message to another user
        found = False
        # creates a variable to check if the user was not found and prints once
        for x in self.userList:
            if message.target == x.username:
                # checks is the account recieving the message exsists
                x.mailbox.append(message)
                # if the account does exist, attach the mail.
                found = True
                print('message sent')
            else:
                pass
        if found == False:
            print("user not found")

    def addFriend(self,manager):
        friend = input("Who would you like to add?")
        found = False
        while found == False:
            for x in manager.userList:
                if friend == x.username:
                    print("Would you like to send a message?")
                    yes = input('Yes or No: ')
                    if yes == 'yes':
                        message = input("message: ")
                    elif yes == 'no':
                        message = ' '
                    else:
                        message = yes
                    possibleFriend = mail('friendRequest', self, friend, message)
                    manager.send(possibleFriend)
                    found = True
                else:
                    pass
            if found == False:
                print("that person was not found")
                friend = input("try again?")
                if friend == 'yes':
                    friend = input("Username: ")
                elif friend == 'no':
                    found = True
                else:
                    print('please enter yes or no')
                    friend = input(': ')
class mail():
    #for all forms of communication between users
    def __init__(self,notification,sender,target,content=' '):
        #Notification is the type of mail, sender is sender, target is reciever and content is if it has a message
        self.notification=notification
        self.content=content
        self.sender=sender
        self.target=target
    def __str__(self):
        return 'Message from {}'.format(self.sender.username)
    def displayMail(self):
        #Only displays mail currently
        print(self.content)
        print(f"from {self.sender.username}")
    def friendRequest(self,user):
        #Attachs usernames to the friend box of each account if accepted
        print('you have recieved a friend request from {}'.format(self.sender.username))
        if self.content != ' ':
            #If the message is not blank, print the message
            print("message attached: {}".format(self.content))
        answer=input("Would you like to accept the friend request: ")
        test=False
        while test==False:
            if answer=='yes':
                #if accepted, append friend onto each account
                user.friends.append(self.sender.username)
                self.sender.friends.append(user.username)
                print(f"{user.username} has become friends with {self.sender.username}")
                test=True
            elif answer=='no':
                print("You have not accepted the request.")
                test=True
            else:
                pass
                answer=input("yes or no: ")
    def checkMail(self,user):
        #may end up moving this to user class
        for x in user.mailbox:
            if self.notification=='mailing':
                displayMail()
            elif self.notification=='friendRequest':
                self.friendRequest(user)
            else:
                pass
class community():
    def __init__(self):
        self.name=''
        self.members=[]
        self.description=''
        self.admin=None
    def createCommunity(self):
        tName=input("What would you like to name the community: ")
class user(mainManager):
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.community=None
        self.friends=[]
        self.ban=[]
        self.mailbox=[]
        self.special=None
    def __str__(self):
        return "Username is {}".format(self.username)
    '''def addFriend(self):
        friend=input("Who would you like to add?")
        found=False
        while found==False:
            for x in userlist:
                if friend==x.username:
                    print("Would you like to send a message?")
                    yes=input('Yes or No: ')
                    if yes=='yes':
                        message=input("message: ")
                    elif yes=='no':
                        message=' '
                    else:
                        message=yes
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
                    friend=input(': ')'''
    def checkMail(self):
        #may end up moving this to user class
        for x in self.mailbox:
            if x.notification=='mailing':
                displayMail()
            elif x.notification=='friendRequest':
                x.friendRequest(self)
            else:
                pass
manager=mainManager()
admin=user('atbauchat','Bauchat1')
manager.userList.append(admin)
yo=True
while yo:
    check=input("what would you like to test?")
    if check=='users':
        for x in manager.userList:
            print(x.username)
    elif check=='create new user':
        manager.createNewUser()
    elif check=='add friend':
        print('who would you like to add friend as?')
    elif check=='quit':
        yo=False
