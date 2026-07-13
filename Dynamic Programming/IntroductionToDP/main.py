#Memoization
class Solution1:
    def fib(self, n, dp):
        if n<=1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.fib(n-1, dp)+self.fib(n-2, dp)
        return dp[n]
#Tabulation
class Solution2():
    def fib(self, n):
        if n<=1:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    
if __name__=="__main__":
    sol1=Solution1()
    sol2=Solution2()
    n=10
    dp=[-1]*(n+1)
    fib1=sol1.fib(n, dp)
    fib2=sol2.fib(n)
    print(f"Memoization: {fib1}")
    print(f"Tabulation: {fib2}")
