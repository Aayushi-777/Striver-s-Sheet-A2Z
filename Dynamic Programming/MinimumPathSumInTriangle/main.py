class Solution:
    def min_path_sum_triangle(self, triangle, n):
        dp=[[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            dp[n-1][j]=triangle[n-1][j]
        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                down=triangle[i][j]+dp[i+1][j]
                diag=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(down, diag)
        return dp[0][0]
    
if __name__=="__main__":
    sol=Solution()
    triangle = [
    [1],
    [2, 3],
    [3, 6, 7],
    [8, 9, 6, 10]
    ]
    n=len(triangle)
    ans=sol.min_path_sum_triangle(triangle, n)
    print(f"The minimum sum in the triangle is: {ans}")