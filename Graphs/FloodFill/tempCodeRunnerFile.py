from collections import deque
class Solution:
    def flood_fill(self, image, sr, sc, new_colour):
        rows=len(image)
        cols=len(image[0])
        old_colour=image[sr][sc]
        if old_colour==new_colour:
            return image
        q=deque()
        q.append((sr, sc))
        image[sr][sc]=new_colour
        directions=[(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y=q.popleft()
            for dx, dy in directions:
                nx=x+dx
                ny=y+dy
                if 0<=nx<rows and 0<=ny<cols:
                    if image[nx][ny]==old_colour:
                        image[nx][ny]=new_colour
                        q.append((nx, ny))
        return image
if __name__=="__main__":
    sol=Solution()
    image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr=1
    sc=1
    new_colour=0
    res=sol.flood_fill(image, sr, sc, new_colour)
    print(res)