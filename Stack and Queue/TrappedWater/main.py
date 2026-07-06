class Solution:
    def trap(self, height):
        n=len(height)
        left, right=0, n-1
        max_left=max_right=0
        total_water=0
        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=max_left:
                    max_left=height[left]
                else:
                    total_water+=max_left-height[left]
                left+=1
            else:
                if height[right]>=max_right:
                    max_right=height[right]
                else:
                    total_water+=max_right-height[right]
                right-=1
        return total_water
    
if __name__=="__main__":
    sol=Solution()
    height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ans=sol.trap(height)
    print(f"Trapped water: {ans}")