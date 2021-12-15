import random
import math



contacts={"sriramupi":9837423572,"jeyadevupi":8875374234,"niteshupi":6538429534,"srimanupi":7126432857,"sudhamaliniupi":8756423657,"sundar@upi":8877945681,"rooneyupi":6549871590}

class Gpay:

    def __init__(self):
        self.pay=input("Enter Number Or ID To Whom You Want To Pay:")

    def payment(self):
        if(self.pay.isnumeric()):
            vv=contacts.values()
            if(int(self.pay) in vv):
                paymentconfirmation()
            else:
                yn=input("Do You Want To Add New Contact y/n?")
                if(yn=='y'):
                    addcontacts()
                else:
                    exit()
        elif(self.pay.isalpha()):
            kv=contacts.keys()
            if(self.pay in kv):
                paymentconfirmation()
            else:
                tn=input("Do You Want To Add New Contact y/n?")
                if(tn=='y'):
                    addcontacts()
                else:
                    exit()

def paymentconfirmation():
    amount=int(input("Enter the Amount to be sent:"))
    key=otpgen()
    print("\n")
    value=int(input("Enter The Received OTP:"))
    print("\n")
    if(key==value):
        print("Transaction Successful")
        print("\n")
        
    else:
        print("Transaction Failed")
        print("\n")
        

def otpgen():
    otp=""
    digits="0123456789"

    for i in range(6):
        otp=otp+digits[math.floor(random.random()*10)]

    print("The OTP is:",otp)

    return (int(otp))


def addcontacts():
    upiid=input("Enter UPI ID:")
    phonenumber=input("Enter Your Phone Number:")
    if(len(phonenumber)==10):
        contacts[upiid]=int(phonenumber)
    else:
        raise ValueError("Number Should Be Of 10 Digits Try Again")
    print("\n")

def viewcontacts():
    for i,j in contacts.items():
        print("         ",i," : ",j)

    print("\n")


def menu():
    print("""
    1.Pay
    2.Add Contacts
    3.View Contacts
    4.Exit App
    """)
    pref=int(input("Enter The Number Of Your Preference:"))
    print("\n")
    if(pref==1):
        ps=Gpay()
        ps.payment()
    elif(pref==2):
        addcontacts()
    elif(pref==3):
        viewcontacts()
    elif(pref==4):
        print("""Thank You For Using Google Pay""")
        exit()


menu()
