class Solution:
    def frog_jump(self, height):
        if not height:
            return 0
        n=len(height)
        dp=[float('inf')]*n
        dp[0]=0
        for ind in range(1, n):
            jump_one=dp[ind-1]+abs(height[ind]-height[ind-1])
            jump_two=float('inf')
            if ind>1:
                jump_two=dp[ind-2]+abs(height[ind]-height[ind-2])
            dp[ind]=min(jump_one, jump_two)
        return dp[n-1]

if __name__=="__main__":
    sol=Solution()
    height=[30, 10, 60, 10, 60, 50]
    mini_en=sol.frog_jump(height)
    print(f"The minimum energy is: {mini_en}")