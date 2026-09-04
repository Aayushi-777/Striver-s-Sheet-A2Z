class Solution:
    def dfs(self, r, c, br, bc, grid, vis, shape):
        vis[r][c]=True
        shape.append((r-br, c-bc))
        directions=[(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            nr=r+dr
            nc=c+dc
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1 and not vis[nr][nc]:
                self.dfs(nr, nc, br, bc, grid, vis, shape)
    def count_dist_islands(self, grid):
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for i in range(n)]
        shapes=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    shape=[]
                    self.dfs(i, j, i, j, grid, vis, shape)
                    shapes.add(tuple(shape))
        return len(shapes)
if __name__=="__main__":
    sol=Solution()
    grid=[
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]
    ans=sol.count_dist_islands(grid)
    print(ans)
    