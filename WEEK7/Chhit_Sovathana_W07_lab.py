file_path = "W07_text.txt"

class FileManager:
    def create_file(self):
        try:
            with open(file_path, "x") as file:
                print(f"File {file_path} created successfully.")
        except FileExistsError:
            print("File already exists.")
        finally:
            print("File creation process completed.")

    def write_to_file(self):
        items = input("Enter items separated by commas: ").split(",")
        try:
            with open(file_path, "w") as file:
                for item in items:
                    file.write(item.strip() + "\n")
                print(f"Data written successfully to {file_path}.")
        except FileNotFoundError:
            print("File doesn't exist.")
        finally:
            print("Write operation completed.")

    def read_file(self):
        try:
            with open(file_path, "r") as file:
                print("File Content:")
                print(file.read())
        except FileNotFoundError:
            print("File doesn't exist.")
        finally:
            print("Read operation completed.")

    def file_to_dict(self):
        data = {}
        try:
            with open(file_path, "r") as file:
                for i, line in enumerate(file, start=1):
                    data[i] = line.strip()
        except FileNotFoundError:
            print("File doesn't exist.")
        finally:
            print("Convert File successfully.")
        return data


class FileUpdate(FileManager):
    def add(self, data):
        item = input("Enter a new item: ").strip()
        
        if not data:
            new_id = 1
        else:
            new_id = max(data.keys()) + 1
            
        data[new_id] = item

        with open(file_path, "w") as file:
            for value in data.values():
                file.write(value + "\n")

        print(f"Current Data: {data}")
        print("Add operation completed.")

    def update(self, data):
        key = int(input("Enter key item: "))

        if key not in data:
            print("Key not found!")
            return

        item = input("Enter a new item: ").strip()
        data[key] = item

        with open(file_path, "w") as file:
            for value in data.values():
                file.write(value + "\n")

        print(f"Current Data: {data}")
        print("Update operation completed.")

    def delete(self, data):
        key = int(input("Enter key item: "))

        if key not in data:
            print("Key not found!")
            return

        data.pop(key)

        with open(file_path, "w") as file:
            for value in data.values():
                file.write(value + "\n")

        print(f"Current Data: {data}")
        print("Delete operation completed.")


fm = FileManager()
fu = FileUpdate()

def run():
    data = fm.file_to_dict()
    option = input("Choose an action (add / update / delete / read): ").lower()

    if option == "add":
        fu.add(data)
    elif option == "update":
        fu.update(data)
    elif option == "delete":
        fu.delete(data)
    elif option == "read":
        fm.read_file()
    else:
        print("Invalid option.")

run()






# #Exercise 1
# try:
#     file = open("W07TXT","w")
#     print("File Create Successfully!")
#     file.close()
#     UserINput=[]
#     n=int(input("Enter The Element :"))
#     for i in range (n):
#         itme=input("Input Item:")
#         UserINput.append(itme)
#     with open("W07TXT","w") as f:
#         for i in UserINput:
#             f.write(i)
#             f.write("\n")
#     print("Data written successfully to 'W07_Text.txt'")
#     print("write Operation complete")
# except Exception as e:
#     print("An error occurred",e)   
# else:
#     with open("W07TXT", "r") as f:
#         List = [line.strip() for line in f.readlines()]
#         print("\nFile Content :")
#         for i in List:
#             print(i)
#         print("\nFile 'W07_text.txt' Read Successfully!")
#         print("Read Operation Complete")

# finally:
#     print("\nProgram finished.")

# #Exercise 2
# class FileManager:
#     def __init__(self):
#         self.file = r"D:\Y2\T1\PYTHON FOR CYBER\Bonus\W07TXT"

#     def ConvertToDIc(self):
#         ListValue = []
#         countitem= 0
#         with open(self.file, "r") as f:
#             List = f.readlines()
#             for i in List:
#                 count += 1
#                 ListValue.append(count)
#             Dic = dict(zip(ListValue, List))
#         return Dic


# class FileUpdate(FileManager):

#     def add(self):
#         NewItem = input("Enter new Item: ")
#         if not NewItem:
#             raise ValueError("Item cannot be empty.")
#         with open(self.file, 'a') as a:
#             a.write(NewItem + "\n")
#         print("Item added.")

#     def update(self):
#         Dic = self.ConvertToDIc()
#         print("Current items:", Dic)

#         try:
#             key = int(input("Enter the key number to update: "))
#             if key not in Dic:
#                 raise KeyError("Key does not exist.")
            
#             new_value = input("Enter new value: ")
#             if not new_value:
#                 raise ValueError("Value cannot be empty.")

#             Dic[key] = new_value + "\n"

#             with open(self.file, "w") as up:
#                 for value in Dic.values():
#                     up.write(value)

#             print("Item updated.")

#         except ValueError:
#             print("Invalid input. Must be a number.")
#         except KeyError as e:
#             print(e)

#     def delete(self):
#         Dic = self.ConvertToDIc()
#         print("Current items:", Dic)

#         try:
#             key = int(input("Enter key number to delete: "))
#             if key not in Dic:
#                 raise KeyError("Key does not exist.")

#             del Dic[key]

#             with open(self.file, "w") as delete:
#                 for value in Dic.values():
#                     delete.write(value)

#             print("Item deleted.")

#         except ValueError:
#             print("Invalid input. Must be a number.")
#         except KeyError as e:
#             print(e)


# fu = FileUpdate()

# while True:
#     print("1. Add Item")
#     print("2. Update Item")
#     print("3. Delete Item")
#     print("4. Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         fu.add()

#     elif choice == "2":
#         fu.update()

#     elif choice == "3":
#         fu.delete()

#     elif choice == "4":
#         print("Exiting")
#         break

#     else:
#         print("Invalid option. Try again.")