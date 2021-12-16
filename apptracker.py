import sys

data={"nithesh":{"Instagram":30,"Twitter":30,"Spotify":20,"Tunein":20,"Youtube":60},
      "bolt":{"Instagram":60,"Twitter":10,"Spotify":70,"Tunein":5,"Youtube":15}}


class Track:
    """ Digital Wellbeing App"""
    def __init__(self,name):
        self.name=name

    def warningsfunction(self):
        """ Displays The Apps That Your Are Over Using"""
        print("Displaying All The Apps That are Overused\n")
        for key,value in data[self.name].items():
            if value>45:
                print(key,end=" ")
        print("\n")
        menu()

def viewdata():
    """ View Data Process"""
    for key,value in data.items():
        print(key,value)

    print("\n")
    menu()

def menu():
    """ Menu Process """
    temp={}
    print("""
          1.Check For App Tracking Of a Person
          2.Add Your Data For Tracking
          3.View The Data
          4.Exit The App
          """)
    mention=int(input("Please Enter Your Choice:"))
    if mention==1:
        name=input("Enter The Name Of The Person Whom You Want To Track?")
        obj=Track(name)
        obj.warningsfunction()
    elif mention==2:
        pername=input("Enter Your Name:")
        print("\n")
        noofapps=int(input("Enter The Number Of App Data You Want To Add?"))
        for i in range(noofapps):
            appname=input("Enter The App Name:")
            usage=int(input("Enter The Usage In Minutes:"))
            print("\n")
            temp[appname]=usage
        data[pername]=temp
        menu()
    elif mention==3:
        viewdata()
    elif mention==4:
        print("Thank You For Using Digital Wellbeing")
        sys.exit()

menu()
