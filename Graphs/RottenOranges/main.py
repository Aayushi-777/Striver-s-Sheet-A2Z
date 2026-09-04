from collections import deque
class Solution:
    def rotten_oranges(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i, j))
                elif grid[i][j]==1:
                    fresh+=1
        minutes=0
        directions=[(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh>0:
            for k in range(len(q)):
                x, y=q.popleft()
                for dx, dy in directions:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        fresh-=1
                        q.append((nx, ny))
            minutes+=1
        if fresh==0:
            return minutes
        return -1
if __name__=="__main__":
    sol=Solution()
    grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    mins=sol.rotten_oranges(grid) 
    print(mins)