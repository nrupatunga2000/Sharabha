# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536,
# the output shall be “6 3 5 7“, with a space separating the digits.

class Pingu:
    def tanu(self):
        integers = input("enter few integers: ")
        n = ' '.join(integers[::-1])
        print(n)

obj1 = Pingu()
obj1.tanu()

