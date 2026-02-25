class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print("Car details:")
        print(f"  Make : {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Year : {self.year}")
        
C = Car('toyota', 'corola', 2007)
C.display_info()
