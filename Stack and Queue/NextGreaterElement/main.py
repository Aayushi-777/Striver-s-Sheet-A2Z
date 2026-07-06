class Solution:
    def next_greater(self, nums):
        stack=[]
        result=[]
        for i in range(len(nums)):
            result.append(-1)
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if stack:
                result[i]=stack[-1]
            stack.append(nums[i])
        return result
    
if __name__=="__main__":
    sol=Solution()
    nums=[4, 5, 2, 10]
    ans=sol.next_greater(nums)
    print(f"The next greater element is: {ans}")