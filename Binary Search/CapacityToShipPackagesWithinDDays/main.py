class Solution:
    def days_needed(self, weights, capacity):
        days=1
        load=0
        for w in weights:
            if load+w>capacity:
                days+=1
                load=w
            else:
                load+=w
        return days
    def ship_within_days(self, weights, d):
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            days=self.days_needed(weights, mid)
            if days<=d:
                high=mid
            else:
                low=mid+1
        return low
    
if __name__=="__main__":
    sol=Solution()
    weights=[5,4,5,2,3,4,5,6]
    d=5
    ans=sol.ship_within_days(weights, d)
    print(f"The minimum weigh is: {ans}")