class Solution:
    def backtrack(self, start, nums, curr, res):
        res.append(list(curr))
        for i in range(start, len(nums)):
            if i >start and nums[i]==nums[i-1]:
                continue
            curr.append(nums[i])
            self.backtrack(i+1, nums, curr, res)
            curr.pop()
    def subset_with_dup(self, nums):
        nums.sort()
        res=[]
        self.backtrack(0, nums, [], res)
        return res

if __name__=="__main__":
    sol=Solution()
    nums=list(map(int, input().split()))
    ans=sol.subset_with_dup(nums)
    for sub in ans:
        print(sub, end=" ")
    print()