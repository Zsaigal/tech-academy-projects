

# Creating parent class

class vehicle:
    Tires=4
    Color="Black"
    Model=2020
    Make="Honda"

    def information(self):
        company_price= input("Enter company price: ")
        print("This {} vehicle is worth ${}".format(self.Make,company_price))

# Child class

class bike(vehicle):
    Tires=2
    Color="Grey"
    Model=2005
    Make="Suzuki"
    Mileage="10000kms"
    Owner_name="Harry"

    def information(self):
        company_price= input("Enter company price: ")
        print("This {} bike, owned by {} is worth ${} and is driven approximately {}".format(self.Make,self.Owner_name,company_price,self.Mileage))

# Another Child class

class boat(vehicle):
    Tires=0
    Color="White"
    Model=2010
    Mileage="500kms"
    type_of_boat="Speedboat"


    def information(self):
        company_price= input("Enter company price: ")
        print("This {} {} boat is worth ${}".format(self.Make,self.type_of_boat,company_price))






if __name__=="__main__":
    x=vehicle()
    x.information()

    y=bike()
    y.information()

    z=boat()
    z.information()
