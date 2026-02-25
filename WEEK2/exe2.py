mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def squareNumbers(mylist):
    newlist = []
    for i in range(len(mylist)):
        if mylist[i] % 2 == 0:
            newlist.append(mylist[i] * mylist[i])
    return newlist
print(squareNumbers(mylist))








# newlist=[]
# for i in range(len(mylist)):
#     if (mylist[i]%2==0):
#         newlist.append(mylist[i]*mylist[i])
# print(newlist)