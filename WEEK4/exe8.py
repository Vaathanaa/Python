class PhoneBook:
    def __init__(self):
        self.contacts = {} 
    def add_contact(self, name, number):
        print(f"Added contact: {name} -> {number}")
        self.contacts[name] = number
    def find_contact(self, name):
        if name in self.contacts:
            print(f"{name}'s number: {self.contacts[name]}")
        else:
            print(f"{name} can't found in phone book.")
pb = PhoneBook()
pb.add_contact("John", "+855811314573")
pb.add_contact("Jane", "+855826481946")
pb.find_contact("John")
pb.find_contact("Alice")
pb.find_contact("Jane")