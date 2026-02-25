class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
    def add_student(self, name):
        print(f"Added student: {name}")
        self.students.append(name)
    def list_students(self):
        print(f"Students in {self.class_name}:")
        for student in self.students:
            print(f" {student}")
room = Classroom("Math 101")
room.add_student("Alice")
room.add_student("Bob")
room.add_student("Charlie")
room.list_students()