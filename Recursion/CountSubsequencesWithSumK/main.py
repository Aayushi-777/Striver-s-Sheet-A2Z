class Solution:
    def func(self, ind, sum, nums):
        if sum==0:
            return 1
        if sum<0 or ind==len(nums):
            return 0
        return self.func(ind+1, sum-nums[ind], nums)+self.func(ind+1, sum, nums)
    def count_subsequences(self, nums, target):
        return self.func(0, target, nums)
if __name__=="__main__":
    sol=Solution()
    nums=[1, 2, 3, 4, 5]
    target=5
    ans=sol.count_subsequences(nums, target)
    print(f"The number of subsequences with sum {target} is: {ans}")