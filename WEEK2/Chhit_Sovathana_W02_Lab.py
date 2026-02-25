#exercise1
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

#exercise2
mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def squareNumbers(mylist):
    newlist = []
    for i in range(len(mylist)):
        if mylist[i] % 2 == 0:
            newlist.append(mylist[i] * mylist[i])
    return newlist
print(squareNumbers(mylist))

#exercise3
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

#exercise4
mytuple=(10,5,8,12,13)
def find_min_max(mytuple : tuple):
    lowest=mytuple[0]
    highest=mytuple[0]
    for i in mytuple:
        if i < lowest:
            lowest =i 
        elif i>highest:
            highest=i
    return [highest,lowest]
print(find_min_max(mytuple))

#exercise5
citydata = [
    ("Phnom Penh",11.5564,104.9282),
    ("Siem Reap",13.3622,103.8597)
]
def displaydata(data_list):
    for city_name, latitude, longitude in data_list:
        print(f"City: {city_name}, Latitude: {latitude}, Longitude: {longitude}")
displaydata(citydata)

#exercise6
mydict = {1:10,2:20,3:30,4:40}
def douple_value(mydict):
    x = lambda a : a*2
    for i in mydict:
        mydict[i] = x(mydict[i])
    return mydict        
print(douple_value(mydict))

#exercise7
text = input("Enter your word:")
mydict ={}
def countFrequency(text):
    for char in text:
        if char in mydict:
            mydict[char] += 1
        else:
            mydict[char] = 1
    return mydict
print(countFrequency(text))

#exercise8
mydict1={'a':1,'b':3,'c':5}
mydict2={'a':5,'b':2,'c':4}
def mergeValue(dict1, dict2):
    merge = dict1.copy()
    merge.update(dict2)
    return merge
print(mergeValue(mydict1, mydict2))