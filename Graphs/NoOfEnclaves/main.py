from collections import deque
class Solution:
    def no_of_enclaves(self, grid):
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for i in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if grid[i][j]==1 and not vis[i][j]:
                        vis[i][j]=True
                        q.append((i, j))
        directions=[(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            r, c=q.popleft()
            for dr, dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1 and not vis[nr][nc]:
                    vis[nr][nc]=True
                    q.append((nr, nc))
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    count+=1
        return count
if __name__=="__main__":
    sol=Solution()
    grid=[
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    ans=sol.no_of_enclaves(grid)
    print(ans)