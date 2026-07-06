class Solution:
    def sumofn(self, n):
        if n==0:
            return 0
        return n+self.sumofn(n-1)
if __name__=="__main__":
    n=10
    sol=Solution()
    result=sol.sumofn(n)
    print(f"The sum of first {n} numbers is: {result}")
