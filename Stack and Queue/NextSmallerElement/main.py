class Solution:
    def next_smaller(self, nums):
        stack=[]
        result=[-1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1]>=nums[i]:
                stack.pop()
            if stack:
                result[i]=stack[-1]
            stack.append(nums[i])
        return result

if __name__=="__main__":
    sol=Solution()
    arr=[1, 3, 2, 4]
    ans=sol.next_smaller(arr)
    print(f"The next smaller element is: {ans}")