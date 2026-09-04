from collections import deque
class Solution:
    def nearest(self, grid):
        n=len(grid)
        m=len(grid[0])
        dist=[[0]*m for i in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    q.append((i, j))
        directions=[(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            r, c=q.popleft()
            for dr, dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m:
                    if grid[nr][nc]==0 and dist[nr][nc]==0:
                        dist[nr][nc]=dist[r][c]+1
                        q.append((nr, nc))
        return dist

if __name__=="__main__":
    sol=Solution()
    grid=[[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
    ans=sol.nearest(grid) 
    for row in ans:
        print(*row)