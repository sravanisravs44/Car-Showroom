class carshowroom:
    def _init_(self,cgst,sgst,insurance):
        self.cgst = cgst
        self.sgst = sgst
        self.insurance = insurance

    def company(self):
        while True:
            print("toyota")
            print("mahindra")
            print("mercedes")
            self.carcompany = input("enter a car company")
            if self.carcompany == "toyota":
                print("welcome to ", self.carcompany)
                print("innova")
                print("fortuner")
                break
            elif self.carcompany == "mahindra":
                print("welcome to ", self.carcompany)
                print("scorpio")
                print("thar")
                break
            elif self.carcompany == "mercedes":
                print("welcome to ", self.carcompany)
                print("Gwagen")
                print("AMG")
                break
            else:
                print("enter valid company")

    def model(self):
        while True:
            self.carmodel = input("enter a car model")
            if self.carcompany == "toyota" and self.carmodel == "innova":
                break
            elif self.carcompany == "toyota" and self.carmodel == "fortuner":
                break
            elif self.carcompany == "mahindra" and self.carmodel == "scorpio":
                break
            elif self.carcompany == "mahindra" and self.carmodel == "thar":
                break
            elif self.carcompany == "mercedes" and self.carmodel == "Gwagen":
                break
            elif self.carcompany == "mercedes" and self.carmodel == "AMG":
                break
            else:
                print("enter a valid car model")

    def price(self):
        while True:
            if self.carmodel == "innova":
                srp = 3000000
                break
            elif self.carmodel == "fortuner":
                srp = 3300000
                break
            elif self.carmodel == "scorpio":
                srp = 2450000
                break
            elif self.carmodel == "thar":
                srp = 1120000
                break
            elif self.carmodel == "Gwagen":
                srp = 30000000
                break
            elif self.carmodel == "AMG":
                srp = 7100000
                break
            else:
                print("invalid")

        onroadprice = (srp)+(srp*((self.cgst)/100)) + \
            (srp*((self.sgst)/100))+(self.insurance)
        print(onroadprice)
obj1=carshowroom(18,18,100000)
obj1.company()
obj1.model()
obj1.price()
