class Solution:
    def can_jump(self, nums):
        max_index=0
        for i in range(len(nums)):
            if i>max_index:
                return False
            max_index=max(max_index, i+nums[i])
        return True

if __name__=="__main__":
    sol=Solution()
    nums=[4, 3, 7, 1, 2]
    ans=sol.can_jump(nums)
    print(f"Can reach the last index?: {ans}")