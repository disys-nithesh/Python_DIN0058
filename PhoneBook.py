class phonebook:
    
    contact={}
    favourite=[]
    recent=[]
    
    def __init__(self,fname:str,lname:str,phno1:int,phno2:int,email:str,ph1typ:str,ph2typ:str):
        if isinstance(fname,str) and isinstance(lname,str) and isinstance(phno1,int) and isinstance(phno2,int) and isinstance(email,str) and isinstance(ph1typ,str) and isinstance(ph2typ,str):
            if len(str(phno1))==10 and len(str(phno2))==10 and email[-10:]=="@gmail.com":
                self.name=fname+" "+lname
                self.ph1=phno1
                self.ph2=phno2
                self.mail=email
                self.type1=ph1typ
                self.type2=ph2typ
                self.add()
            else:
                raise ValueError("data is invalid")
        else:
            raise TypeError("invalid data type")
        
    def add(self):
        self.contact[self.name]=[self.ph1,self.ph2,self.mail,self.type1,self.type2]
        print(f"{self.name}'s contact details added successfully")

    def delete(self,fname:str,lname:str):
        name=fname+" "+lname
        if isinstance(name,str):
            if name in self.contact:
                del self.contact[name]
                print(f"{self.name}'s contact details deleted")
            else:
                raise ValueError("data not present")
        else:
            raise TypeError("invalid data type")

    def search(self,fname:str,lname:str,item:str):
        name=fname+" "+lname
        if isinstance(name,str):
            if name in self.contact:
                lst=self.contact[name]
                self.recent.append(name)
                if item == "number1" or item == "num1" or item == "number" or item == "ph1" or item == "contact":
                    print(f"name : {lst[0]}({lst[3]})")
                elif item == "number2" or item == "num2" or item == "ph2":
                    print(f"name : {lst[1]}({lst[4]})")
                elif item == "mail" or item == "email":
                    print(f"name : {lst[2]}")
                else:
                    raise ValueError("invalid input")
            else:
                raise ValueError("data not present")
        else:
            raise TypeError("invalid data type")

    def rec(self):
        print("Contact History:")
        for i in reversed(self.recent):
            print(f"{i}:{self.contact[i]}")

    def fav(self,fname,lname):
        name=fname+" "+lname
        if isinstance(name,str):
            if name in self.contact:
                self.favourite.append(name)
            else:
                raise ValueError("data not present")
        else:
            raise TypeError("invalid data type")

        print("Favourite Contacts:")
        for i in reversed(self.favourite):
            print(f"{i}:{self.contact[i]}")
                
    def allcont(self):
        print("ALL STORED CONTACTS : ")
        print(self.contact)

    def __del__(self):
        del self.name
        del self.ph1
        del self.ph2
        del self.mail
        del self.type1
        del self.type2
            
nithesh=phonebook("Nithesh","N",9944940877,9966023376,"nithesh7477@gmail.com","Home","Office")
bolt=phonebook("bolt"," ",9911111111,7791123376,"bolt77@gmail.com","Home","Office")
sriman=phonebook("sriman","s",9922222222,7794223376,"sriman77@gmail.com","Home","Office")
rohit=phonebook("rohit","p",9933333333,5594023376,"sriram77@gmail.com","Home","Office")
sriram=phonebook("sriram","s",9944444444,8894023376,"jd77@gmail.com","Home","Office")
jd=phonebook("j","d",9944945557,9994023376,"ak@gmail.com","Home","Office")
ak=phonebook("a","k",9944977377,7794023886,"naren@gmail.com","Home","Office")
naren=phonebook("naren","kumar",9967543377,7767023376,"ahmed@gmail.com","Home","Office")
ahmed=phonebook("ahmed","k",9912343377,7794883376,"akash@gmail.com","Home","Office")
akash=phonebook("akash","agent",6644943377,8894023376,"rohit77@gmail.com","Home","Office")
nithesh.allcont()
#nithesh.delete("Nithesh","N")
#nithesh.search("Nithesh","N","num1")
#nithesh.fav("Nithesh","N")
nithesh.__del__()

#bolt=phonebook("bolt"," ",9944943377,7794023376,"bolt77@gmail.com","Home","Office")
#bolt.allcont()
#bolt.search("bolt"," ","num1")
#bolt.rec()
