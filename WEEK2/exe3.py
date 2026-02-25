index1 = int(input("Enter the Index:"))
firstList=[]
for i in range(index1):
    element = input("Enter the element:")
    firstList.append(element)
index2 = int(input("Enter the Index:"))
secondList=[]
for i in range(index2):
    element = input("Enter the element:")
    secondList.append(element)
def merge(firstList, secondList):
    thirdList = firstList.copy()
    firstSet = set(firstList)
    for item in secondList:
        if item not in firstSet:
            thirdList.append(item)
    return thirdList
print(merge(firstList,secondList))  
    
    
    
    
    
# thirdlist=firstList
# firstset = set(firstList)
# for i in range(index2):
#     if(secondList[i] not in firstset):
#         thirdlist.append(secondList[i])
# print(thirdlist) 
        
    
    
