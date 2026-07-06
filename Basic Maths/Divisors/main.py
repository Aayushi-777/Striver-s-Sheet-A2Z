class Solution:
    def getDivisors(self, n):
        result=[]
        for i in range(1, n+1):
            if n%i==0:
                result.append(i)
        print(f"The divisors of {n} are: {result}")
if __name__=="__main__":
    sol=Solution()
    n=45
    sol.getDivisors(n)