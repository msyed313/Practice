class Car:
    total_cars=0
    def __init__(self,brand,model,fueltype):
        self.__brand=brand
        self.__model=model
        self.__fueltype=fueltype
        Car.total_cars+=1
    def get_brand(self):
        #print(f"This is {self.__model} car of {self.__brand} ")
        return self.__brand
    def get_fueltype(self):
        #print(f"This is {self.__model} car of {self.__brand} ")
        return self.__fueltype
    def get_model(self):
        return self.__model
    @property
    def model(self):
        return self.__model
    @staticmethod
    def general_description():
         return "Source of transport"
class ElectricCar(Car):
    def __init__(self,brand,model,fueltype,battery_size):
        super().__init__(brand,model,fueltype)
        self.battery_size=battery_size
    def name(self):
         print(f"This is {self.get_model()} car of {self.get_brand()} with battery size of {self.battery_size}.")
    def fueltype(self):
        print("This is battery type car")
print("Gives your car information!!!")
brand=input("Enter ur car brand")
model=input("Enter ur car model:")
fuel=input("Enter ur car fuel type:")
mycar=Car(brand,model,fuel)
#mycar.model="city"
print(f"This is {mycar.get_model()} car of {mycar.get_brand()} with {mycar.get_fueltype()} fuel")
print(mycar.general_description())
print("Gives your electric car information!!!")
brand=input("Enter ur car brand:")
model=input("Enter ur car model:")
battery=input("Enter ur car battery size:")
myeleccar=ElectricCar(brand,model,"battery",battery)
myeleccar.name()
myeleccar.fueltype()
print(myeleccar.general_description())
print(Car.total_cars)