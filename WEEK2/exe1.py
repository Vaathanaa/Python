# index = int(input("Enter the Index"))
# myList=[]
# for i in range(index):
#     element = input("Enter the element")
#     myList.append(element)


# for i in range(0,index//2):
#     temp = myList[i]    
#     myList[i]= myList[index -1 -i]
#     myList[index -1 -i]= temp
# print(myList)

index = int(input("Enter the Index:"))
myList = []
for i in range(index):
    element = input("Enter the element:")
    myList.append(element)
def reverselist(myList):
    index = len(myList)
    for i in range(index // 2):
        temp = myList[i]
        myList[i] = myList[index-1-i]
        myList[index-1-i] = temp
    return myList
print(reverselist(myList))

