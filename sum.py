# if the entered number is odd then return sum of current number and the
# previous number. number is even then return the sum of current and the next number

class Tanu:
    def papu(self,n):

        if n%2 == 0:
            even_sum = n + (n+1)
            print(even_sum)

        else:
            odd_sum = n+(n-1)
            print(odd_sum)
obj_tanu = Tanu()
obj_tanu.papu(int(input("enter number 4")))

