#useing for loop to print
number = [1,2,3,4,5]
for i in number :
    print(i)

number = 1
#using while loop 
while number <= 10:
    if number == 4:
        number += 1
        continue  
    if number == 6:
        break  
    print(number)
    number += 1

