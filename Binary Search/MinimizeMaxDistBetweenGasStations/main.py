class Solution:
    def required_stations(self, dist, arr):
        count=0
        for i in range(1, len(arr)):
            gap=arr[i]-arr[i-1]
            count+=int(gap/dist)
            if gap%dist==0:
                count-=1
        return count
    def minimize_max_dist(self, arr, k):
        low=0
        high=max(arr[i+1] for i in range(len(arr)-1))
        while high-low>1e-6:
            mid=(low+high)/2
            if self.required_stations(mid, arr)>k:
                low=mid
            else:
                high=mid
        return high

if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3, 4, 5]
    k=4
    print(sol.minimize_max_dist(arr, k))
