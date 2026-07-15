class Solution:
    def min_path_sum(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=matrix[i][j]
                else:
                    up=matrix[i][j]
                    if i>0:
                        up+=dp[i-1][j]
                    else:
                        up+=int(1e9)
                    left=matrix[i][j]
                    if j>0:
                        left+=dp[i][j-1]
                    else:
                        left+=int(1e9)
                    dp[i][j]=min(up, left)
        return dp[m-1][n-1]

if __name__=="__main__":
    sol=Solution()
    matrix=[
    [5, 9, 6],
    [11, 5, 2]
    ]
    ans=sol.min_path_sum(matrix)
    print(f"The minimum sum is: {ans}")