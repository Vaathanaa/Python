class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Animal Name: {self.name}")
        print(f"Animal age: {self.age}")
a1 = Animal("Leo",4)
a1.show_info()