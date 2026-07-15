class Solution:
    def max_chocolates(self, n, m, grid):
        dp=[[[0 for i in range(m)] for j in range(m)] for k in range(n)]
        for j1 in range(m):
            for j2 in range(m):
                if j1==j2:
                    dp[n-1][j1][j2]=grid[n-1][j1]
                else:
                    dp[n-1][j1][j2]=grid[n-1][j1]+grid[n-1][j2]
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi=-10**9
                    curr=grid[i][j1] if j1==j2 else grid[i][j1]+grid[i][j2]
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            newj1, newj2=j1+dj1, j2+dj2
                            if 0<=newj1<m and 0<=newj2<m:
                                maxi=max(maxi, curr+dp[i+1][newj1][newj2])
                            else:
                                maxi=max(maxi, -10**9)
                    dp[i][j1][j2]=maxi
        return dp[0][0][m-1]
    
if __name__=="__main__":
    sol=Solution()
    grid=[
        [2, 3, 1, 2],
        [3, 4, 2, 2],
        [5, 6, 3, 5]
        ]
    n, m=len(grid), len(grid[0])
    ans=sol.max_chocolates(n, m, grid)
    print(f"The max chocolates picked by both are: {ans}")