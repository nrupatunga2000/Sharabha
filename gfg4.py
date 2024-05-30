#find whether the entered string is symetrical and Palindrom

str1 = input("enter a word/number: ")
lstr = str1.lower()

if len(lstr)%2==0:
    print(f"{str1} is symetrical")
else:
     print(f"{str1} is not Symetrical")
    
if lstr ==lstr[::-1]:
    print(f"{str1} is Palindrom")
else: 
    print(f"{str1} is not palindrom")