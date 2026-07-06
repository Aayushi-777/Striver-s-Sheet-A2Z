class Solution:
    def can_place(self, stalls, cows, d):
        n=len(stalls)
        count=1
        lastpos=stalls[0]
        for i in range(1, n):
            if stalls[i]-lastpos>=d:
                count+=1
                lastpos=stalls[i]
            if count>=cows:
                return True
        return False
    def aggressive_cows(self, stalls, cows):
        stalls.sort()
        low, high=1, stalls[-1]-stalls[0]
        ans=0
        while low<=high:
            mid=(low+high)//2
            if self.can_place(stalls, cows, mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
    
if __name__=="__main__":
    sol=Solution()
    stalls=[1, 2, 8, 4, 9]
    cows=3
    ans=sol.aggressive_cows(stalls, cows)
    print(f"The minimum distance between two cows is: {ans}")