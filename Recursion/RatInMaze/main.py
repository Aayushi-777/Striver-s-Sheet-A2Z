class Solution:
    def is_safe(self, x, y, n, maze, visited):
        return(0<=x<n and 0<=y<n and maze[x][y]==1 and visited[x][y]==0)
    def solve(self, x, y, n, maze, visited, path, res):
        if x==n-1 and y==n-1:
            res.append(path)
            return
        visited[x][y]=1
        if self.is_safe(x+1, y, n, maze, visited):
            self.solve(x+1, y, n, maze, visited, path+"D", res)
        if self.is_safe(x, y-1, n, maze, visited):
            self.solve(x, y-1, n, maze, visited, path+"L", res)
        if self.is_safe(x-1, y, n, maze, visited):
            self.solve(x-1, y, n, maze, visited, path+"U", res)
        if self.is_safe(x, y+1, n, maze, visited):
            self.solve(x, y+1, n, maze, visited, path+"R", res)
        visited[x][y]=0
    def find_path(self, maze, n):
        res=[]
        visited=[[0]*n for _ in range(n)]
        if maze[0][0]==1:
            self.solve(0, 0, n, maze, visited, "", res)
        return res

if __name__=="__main__":
    sol=Solution()
    maze=[
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
    n=len(maze)
    paths=sol.find_path(maze, n)
    print(*paths)