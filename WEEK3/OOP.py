
class Animal:
    def eat(self):
        print("Animals can eat")

class Dog(Animal):
    def bark(self):
        print("Dog can bark")
d = Dog()
d.eat()   
d.bark()  
# #OutPut
# #Animals can eat  
# #Dog can bark
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
for a in [Dog(), Cat()]:
    a.speak()
# #Output
# Dog barks
# Cat meows
