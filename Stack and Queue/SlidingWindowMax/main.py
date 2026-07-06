from collections import deque
from typing import List
class Solution:
    def max_sliding_window(self, nums, k):
        dq=deque()
        result=[]
        for i in range(len(nums)):
            if dq and dq[0]<=i-k:
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                result.append(nums[dq[0]])
        return result
    
if __name__=="__main__":
    sol=Solution()
    arr=[4, 0, -1, 3, 5, 3, 6, 8]
    k=3
    ans=sol.max_sliding_window(arr, k)
    print(*ans)
        