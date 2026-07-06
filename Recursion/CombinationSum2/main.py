class Solution:
    def backtrack(self, sum, last, nums, k, ans):
        if sum==0 and len(nums)==k:
            ans.append(list(nums))
            return
        if sum<=0 or len(nums)>k:
            return
        for i in range(last, 10):
            if i<=sum:
                nums.append(i)
                self.backtrack(sum-i, i+1, nums, k, ans)
                nums.pop()
            else:
                break
    def combination_sum(self, k, n):
        ans=[]
        nums=[]
        self.backtrack(n, 1, nums, k, ans)
        return ans

if __name__=="__main__":
    sol=Solution()
    k=3
    n=9
    res=sol.combination_sum(k, n)
    print(*res)