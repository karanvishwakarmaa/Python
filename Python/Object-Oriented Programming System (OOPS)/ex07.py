class Car:
    @staticmethod
    def start():
        print("car strted..")

    @staticmethod
    def sto():
        print("Car Stoop!!!")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.start())