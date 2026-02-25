class Student():
    def __init__(self,name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade
    def update_grade(self,new_grade):
        print("before update")
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"grade = {self.grade}")
        
        self.grade = new_grade
        print("After update")
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"grade = {self.grade}")        
S1=Student('vathana', 18, 'B')
S1.update_grade('A')