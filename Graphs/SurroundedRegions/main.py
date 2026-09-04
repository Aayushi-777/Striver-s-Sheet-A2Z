class Solution:
    def dfs(self, r, c, mat, vis):
        n=len(mat)
        m=len(mat[0])
        vis[r][c]=1
        directions=[(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr=r+dr
            nc=c+dc
            if 0<=nr<n and 0<=nc<m and mat[nr][nc]=='O' and vis[nr][nc]==0:
                self.dfs(nr, nc, mat, vis)
    def fill(self, n, m, mat):
        vis=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if mat[i][j]=='O' and vis[i][j]==0:
                        self.dfs(i, j, mat, vis)
        for i in range(n):
            for j in range(m):
                if mat[i][j]=='O' and vis[i][j]==0:
                    mat[i][j]='X'
        return mat
if __name__=="__main__":
    sol=Solution()
    mat=[
        ['X','X','X','X'],
        ['X','O','X','X'],
        ['X','O','O','X'],
        ['X','O','X','X'],
        ['X','X','O','O']
    ]
    ans=sol.fill(len(mat), len(mat[0]), mat)
    for row in ans:
        print(*row)