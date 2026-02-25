mydict = {1:10,2:20,3:30,4:40}
def douple_value(mydict):
    x = lambda a : a*2
    for i in mydict:
        mydict[i] = x(mydict[i])
    return mydict        
print(douple_value(mydict))