#exercise 1
# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))

# print(f"Sum={a+b}")
# print(f"Different={a-b}")   
# print(f"Product={a*b}")
# print(f"Quotient={a/b}")

#exercise 2

# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))
# c = int(input("Enter the third number"))

# def compare(a,b):
#     if (a>b):
#         return a
#     else:
#         return b
    
# print("The largest number is =", compare(compare(a, b), c))

# Exercise 3

# for i in range (1,101):
#     if(i%3 ==0):
#         print("Fizz")
#     elif (i%5 ==0):
#         print("Buzz")
#     elif (i%5==0 and i%3==0):
#         print("FizzBuzz")
#     else:
#         print(i)

# Exersie 4

# a = int(input("Enter the  number"))
# b = 1
# for i in range(1, a + 1):
#     b = b * i
# print("The factorial is", b)

# Exercise 5

# text = input("Enter a string")
# palindrome = 1
# for i in range(len(text)//2):
#     if(text[i] != text[-(i-1)]):
#         palindrome = 0        
# if palindrome:
#     print(f"(text) is palindrome")
# else:
#      print(f"(text) isn't palindrome")