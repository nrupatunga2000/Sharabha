# Exercise 15: Write a function called exponent(base, exp)
# that returns an int value of base raises to the power of exp.

class Tanu:
    def exponent(self,base,exponent):
        result = (base**exponent)
        print(f'{base} raise to the power of {exponent} is {result}')

papu = Tanu()
papu.exponent(int(input('enter base:')),int(input('enter exponent :')))
