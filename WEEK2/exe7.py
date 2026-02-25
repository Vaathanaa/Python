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