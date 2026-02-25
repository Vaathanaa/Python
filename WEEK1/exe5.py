text = input("Enter a string")
palindrome = 1
for i in range(len(text)//2):
    if(text[i] != text[-(i-1)]):
        palindrome = 0
        
if palindrome:
    print(f"(text) is palindrome")
else:
     print(f"(text) isn't palindrome")