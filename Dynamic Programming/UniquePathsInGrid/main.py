class Solution:
    def solve(self, m, n, dp):
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                    continue
                up=0
                left=0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
        return dp[m-1][n-1]
    def unique_paths(self, m, n):
        dp=[[0]*n for i in range(m)]
        return self.solve(m, n, dp)
    
if __name__=="__main__":
    sol=Solution()
    m=3
    n=2
    ans=sol.unique_paths(m, n)
    print(f"The number of unique paths in the grid of size {m}*{n} is: {ans}")
