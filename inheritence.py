class car:
    @staticmethod
    def car_info():
        print("This is a car")
       
        
    @staticmethod
    def car_speed():
        print("Max speed is 200km/hr")
        
class bmw(car):
    def __init__ (self,model,year):
        self.model=model
        self.year=year
        
car1=bmw("X5",2020)
car2=bmw("X3",2019)

print(car1.car_info())