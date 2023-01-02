#Fibonacci Series using recursion

class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        if A==1:
            return 1
        if A==0:
            return 0
        return self.findAthFibonacci(A-1)+self.findAthFibonacci(A-2)
