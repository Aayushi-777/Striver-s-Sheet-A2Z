class Solution:
    def solve(self, nums):
        prev=0
        prev2=0
        for money in nums:
            curr=max(prev, prev2+money)
            prev2=prev
            prev=curr
        return prev
    def rob_street(self, arr):
        if len(arr)==1:
            return arr[0]
        return max(self.solve(arr[:-1]), self.solve(arr[1:]))

if __name__=="__main__":
    sol=Solution()
    arr=[1, 5, 1, 2, 6]
    loot=sol.rob_street(arr)
    print(f"The maximum loot is: {loot}")