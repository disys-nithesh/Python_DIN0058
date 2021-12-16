database={"sriman@gmail.com":"sriman7477","jayavardhan@gmail.com":"jv3763","nithesh7477@gmail.com":"nithesh7477","sriram@gmail.com":"sriram1234","jd12@gmail.com":"jeyadev2001"}
class facebook:

    friendlist=[]
    groups={}

    def __init__(self):
        self.enter=input("******Login or SignUp****** : ")
        print()
        self.user()
        
    def user(self):
        if self.enter =="Login" or self.enter =="login":
            print("Login to Facebook : ")
            print()
            self.username=input("Enter Your Mail Id : ")
            self.password=input("Enter Your Password : ")
            if isinstance(self.username,str) and isinstance(self.password,str):
                if self.username in database and database[self.username]==self.password:
                    print()
                    print("*** Logged In Successfully ***")
                    print()
                    self.add()
                else:
                    raise ValueError("Invalid input")
            else:
                raise TypeError("Invalid Datatype")
            
        elif self.enter == "SignUp" or self.enter == "Signup" or self.enter == "signup":
            print("SignUp to Facebook : ")
            print()
            self.username=input("Enter Your Username : ")
            self.mail=input("Enter Your E-mail : ")
            self.password=input("Enter Your Password : ")
            if isinstance(self.username,str) and isinstance(self.mail,str) and isinstance(self.password,str):
                if self.mail[-10:] == "@gmail.com" and self.password.isalnum() == True:
                    database[self.mail]=self.password
                    print()
                    print("*** Signed Up Successfully ***")
                    print()
                    self.add()
                else:
                    raise ValueError("Invalid input")
            else:
                raise TypeError("Invalid Datatype")
                    
        
    def add(self):
        print("*****Add Friends******")
        print()
        num=int(input("Number of Friends you want to add : "))
        print()
        for i in range(num):
            name=input("Enter Friends facebook id : ")
            self.friendlist.append(name)
        self.group()    
        

    def group(self):
        print()
        opt=input("Do You Want To Create A Group (y/n) : ")
        print()
        if opt == "y":
            name=input("Enter Group Name : ")
            print()
            self.allfriends()
            print()
            num=input("Number Of Members You Want In Group : ")
            print()
            lst=[]
            for i in range(int(num)):
                frnd=int(input("Select Friend : "))
                lst.append(self.friendlist[frnd-1])
            self.groups[name]=lst
            print()
            print(f"___{name} Members Are___")
            self.printgrp()
        elif opt == "n":
            print("Thank You")

    def printgrp(self):
        print()
        for i,j in self.groups.items():
            for k in range(len(j)):
                print(f"{k+1} : {j[k]}")
        print()
        self.group()

    def allfriends(self):
        print()
        for i in range(len(self.friendlist)):
            print(f"{i+1} : {self.friendlist[i]}")

jv=facebook()


