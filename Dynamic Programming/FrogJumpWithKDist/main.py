class Solution:
    def frog_jump(self, height, k):
        dp=[-1]*(len(height))
        dp[0]=0
        for i in range(1, len(height)):
            min_steps=float('inf')
            for j in range(1, k+1):
                if i-j>=0:
                    jump=dp[i-j]+abs(height[i]-height[i-j])
                    min_steps=min(min_steps, jump)
            dp[i]=min_steps
        return dp[len(height)-1]

if __name__=="__main__":
    sol=Solution()
    height=[30, 10, 60, 10, 60, 50]
    k=2
    ans=sol.frog_jump(height, k)
    print(f"The minimum energy is: {ans}")