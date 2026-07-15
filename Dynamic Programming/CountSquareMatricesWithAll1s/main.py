class Solution:
    def count_squares(self, n, m, arr):
        dp=[[0]*m for i in range(n)]
        for j in range(m):
            dp[0][j]=arr[0][j]
        for i in range(n):
            dp[i][0]=arr[i][0]
        for i in range(1, n):
            for j in range(1, m):
                if arr[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        total=sum(sum(row) for row in dp)
        return total
    
if __name__=="__main__":
    sol=Solution()
    arr=[
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
    ]
    n, m=len(arr), len(arr[0])
    squares=sol.count_squares(n, m, arr)
    print(f"The number of squares of 1s are: {squares}")