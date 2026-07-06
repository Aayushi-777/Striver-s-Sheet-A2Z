class Solution:
    def next_greater(self, nums):
        n=len(nums)
        ans=[-1]*n
        stack=[]
        for i in range(2*n-1, -1, -1):
            ind=i%n
            curr=nums[ind]
            while stack and stack[-1]<=curr:
                stack.pop()
            if i<n:
                if stack:
                    ans[i]=stack[-1]
            stack.append(curr)
        return ans

if __name__=="__main__":
    sol=Solution()
    arr=[5, 7, 1, 7, 6, 0]
    ans=sol.next_greater(arr)
    print(f"The next greater element in circular array is: {ans}")