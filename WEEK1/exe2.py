a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

def compare(a,b):
    if (a>b):
        return a
    else:
        return b
    
print("The largest number is =", compare(compare(a, b), c))