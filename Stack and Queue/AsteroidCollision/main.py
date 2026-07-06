class Solution:
    def asteroid_collision(self, asteroids):
        n=len(asteroids)
        stack=[]
        for i in range(n):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while(stack and stack[-1]>0 and stack[-1]<abs(asteroids[i])):
                    stack.pop()
                if stack and stack[-1]==abs(asteroids[i]):
                    stack.pop()
                elif not stack or stack[-1]<0:
                    stack.append(asteroids[i])
        return stack
        
if __name__=="__main__":
    sol=Solution()
    arr=[10, 20, -10]
    ans=sol.asteroid_collision(arr)
    print(f"The asteroids remaining after collisions are: {ans}")