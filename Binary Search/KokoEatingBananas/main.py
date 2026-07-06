import math
class Solution:
    def calculate_total_hours(self, piles, speed):
        totalH=0
        for bananas in piles:
            totalH+=math.ceil(bananas/speed)
        return totalH
    def min_eating_speed(self, piles, h):
        maxpile=max(piles)
        low, high=1, maxpile
        ans=maxpile
        while low<=high:
            mid=(low+high)//2
            totalH=self.calculate_total_hours(piles, mid)
            if totalH<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

if __name__=="__main__":
    sol=Solution()
    piles=[7, 15, 6, 3]
    h=8
    speed=sol.min_eating_speed(piles, h)
    print(f"The minimum eating speed is: {speed} bananas/hr")