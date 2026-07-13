class Solution:
    def climbing_stairs(self, n):
        dp=[-1]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

if __name__=="__main__":
    sol=Solution()
    n=3
    ways=sol.climbing_stairs(n)
    print(f"The number of ways to reach step 3 is: {ways}")