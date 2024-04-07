#Return the count of a given substring from a string

string = input("enter a srring ")
substring = input("enter the substring for which you need the count: ")

count = string.count(substring)
print(f"{substring} has repeated {count} times in '{string}'ni")
