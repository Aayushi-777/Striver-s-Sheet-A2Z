class Solution:
    def func(self, ind, sum, nums):
        if sum==0:
            return True
        if sum<0 or ind==len(nums):
            return False
        return (self.func(ind+1, sum-nums[ind], nums) or self.func(ind+1, sum, nums))
    def exists_subsequences(self, nums, target):
        return self.func(0, target, nums)
    
if __name__=="__main__":
    sol=Solution()
    nums=[1, 2, 3, 4, 5]
    target=5
    ans=sol.exists_subsequences(nums, target)
    print(f"Is there a subsequence in the array with sum {target}?: {ans}")
                