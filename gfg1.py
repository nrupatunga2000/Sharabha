#Print numbers from 1 to N without the help of loops.

class Tanu:
    def numlen(self,N):
        if N>0:
            self.numlen(N-1)
            print(N,end=' ')

object1 = Tanu()
object1.numlen(N = int(input("enter a number:")))


