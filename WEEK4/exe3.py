class Car:
    def __init__(self,year):
        self.year = year
    def is_vintage(self,carNumber):
        if self.year > 25:
            print(f"Car {carNumber} is vintage : True")
        else:
            print(f"Car {carNumber} is vintage : False")
C1 = Car(23)
C1.is_vintage(1)
C2 = Car(67)
C2.is_vintage(2)