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
