class user_input:
    def __init__(self):
        self.area = input("Enter area: ")

    def h_dis(self,area):
        if self.area == "Avadi":
            self.hot_rate = [{"hotel":"ss hydrabad", "rating":"5-star"},
                        {"hotel":"Guesto Express", "rating":"4.5-star"},
                        {"hotel":"Quality resturant", "rating":"4.3-star"},
                        {"hotel":"A2B", "rating":"4.5-star"}]
        elif self.area == "Porur":
            self.hot_rate = [{"hotel":"Al-taj", "rating":"5-star"},
                        {"hotel":"Manoj bhavan", "rating":"4.9-star"},
                        {"hotel":"Palmshore", "rating":"4.5-star"},
                        {"hotel":"Star briyani", "rating":"4.5-star"}]
        elif self.area == "Thiruvanmaiyur":
            self.hot_rate = [{"hotel":"Salem RR Briyani", "rating":"5-star"},
                        {"hotel":"Shawarma Forest", "rating":"4.7-star"},
                        {"hotel":"SS hydrabad", "rating":"4.4-star"},
                        {"hotel":"Yamoideen", "rating":"4.3-star"}]
        elif self.area == "Tharamani":
            self.hot_rate = [{"hotel":"Takkur Briyani", "rating":"5-star"},
                        {"hotel":"Writes's cafe", "rating":"4.5-star"},
                        {"hotel":"Hotel Saravana Bhavan", "rating":"4.4-star"},
                        {"hotel":"wangs Kitchen", "rating":"4.3-star"}]
        elif self.area == "KK Nagr":
            self.hot_rate = [{"hotel":"Cresent", "rating":"5-star"},
                        {"hotel":"Waf Bites", "rating":"4.9-star"},
                        {"hotel":"Briyani Junction", "rating":"4.5-star"},
                        {"hotel":"Star briyani", "rating":"4.5-star"}]
        elif self.area == "T nagar":
            self.hot_rate = [{"hotel":"Salem RR Briyani", "rating":"5-star"},
                        {"hotel":" Absolute Barbecues T-Nagar", "rating":"4.7-star"},
                        {"hotel":"COAL BARBECUES", "rating":"4.4-star"},
                        {"hotel":"Yamoideen", "rating":"4.3-star"}]
        elif self.area == "Iyyappanthangal":
            self.hot_rate = [{"hotel":"LASSI BISTRO", "rating":"5-star"},
                        {"hotel":"MOGLEE S KITCHEN", "rating":"4.5-star"},
                        {"hotel":"Maa Chandi Hotel", "rating":"4.4-star"},
                        {"hotel":"Shri Balaji Hotel", "rating":"4.3-star"}]
        elif self.area == "Valasaravakkam":
            self.hot_rate = [{"hotel":"Hotel Valasai Subha", "rating":"5-star"},
                        {"hotel":"", "rating":"4.9-star"},
                        {"hotel":"", "rating":"4.5-star"},
                        {"hotel":"Star briyani", "rating":"4.5-star"}]
        elif self.area == "Thiruvanmaiyur":
            self.hot_rate = [{"hotel":"Salem RR Briyani", "rating":"5-star"},
                        {"hotel":"Shawarma Forest", "rating":"4.7-star"},
                        {"hotel":"SS hydrabad", "rating":"4.4-star"},
                        {"hotel":"Yamoideen", "rating":"4.3-star"}]
        elif self.area == "Tharamani":
            self.hot_rate = [{"hotel":"Takkur Briyani", "rating":"5-star"},
                        {"hotel":"Writes's cafe", "rating":"4.5-star"},
                        {"hotel":"Hotel Saravana Bhavan", "rating":"4.4-star"},
                        {"hotel":"wangs Kitchen", "rating":"4.3-star"}]
        else:
            print("Unnable to delivery to your location")
    def disp(self):        
        for i in self.hot_rate:
            f={}
            f=i
            for k,v in f.items():
                print(k,"\t--- \t",v)
                print("--|-------------------|-------------")

class hot_sel(user_input):
    def __init__(self):
        self.uh = input("Enter hotel: ")
        self.h=["hotel1","hotel2","hotel3","hotel4"]
        #fself.di()
        

    def di(self):
        for i in self.h:
            print("\n",i)
                
    def uh_val(self):
        for i in self.h:
            if (i != self.uh):
                raise ValueError("Invalid hotel")
            
class dish(hot_sel):
    def __init__(self):
        self.f=["Chicken Briyani","Chicken Manchuriyan","Parotta","Dosa","Idly"]
        self.disp()
        self.user_dis= input("Enter dish: ")

    def dish_val(self):
        for i in self.f:
            if (i != self.user_dis):
                raise ValueError ("dish is currently unavailable")
                return self.user_dis
            else:
                print("Packing....")
                break
            
    def disp(self):
        print("\n Available dish")
        print("---------------")
        for i in self.f:
            print(i)
class swiggy:
    def __init__(self,area,hotel,dish):
        self.p = area
        self.h = hotel
        self.d = dish
        
    def beforeorder(self):
        print("order details:","from",self.p,"Hotel",self.h,"Dish",self.d)

    def display(self):
        print("order confirmed :",self.d," \n @",self.h," in ",self.p)

class user_dis(swiggy):
    def __init__(self):
        self.bill = 500
        self.sgst = 5
        self.cgst = 10
        self.total = (self.bill+self.sgst+self.cgst)

    def delivery(self):
        self.addr = input("Enter address: ")


    def addvalid(self):
        if isinstance (self.addr,str):
            if isinstance(len(self.addr) <= 25):
                raise ValueError ("enter valid address")
            elif self.addr != None:
                raise ValueError ("invalid address")
                
        
    def display(self):
        print("Delivary address : ",self.addr)
        print("Total bill Rs.",self.total)
        ob1.display()


ob = user_input()
ob.h_dis(ob.area)
ob.disp()
h = hot_sel()
d = dish()
d.dish_val()
ob1 = swiggy(ob.area,h.uh,d.user_dis)
ob1.beforeorder()
ob2 = user_dis()

ob2.delivery()
ob2.addvalid
ob2.display()
