class Solution:
    def solve(self, m, n, matrix, dp):
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    dp[i][j]=0
                    continue
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
    def unique_paths(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*n for i in range(m)]
        ans=self.solve(m, n, matrix, dp)
        return ans

if __name__=="__main__":
    sol=Solution()
    maze=[
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    ans=sol.unique_paths(maze)
    print(f"The number of unique paths to cross the maz is: {ans}")
