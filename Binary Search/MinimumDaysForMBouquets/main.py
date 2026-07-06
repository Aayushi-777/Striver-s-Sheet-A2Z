class Solution:
    def is_possible(self, bloom_days, day, m, k):
        count=0
        bouquets=0
        for bloom in bloom_days:
            if bloom<=day:
                count+=1
                if count==k:
                    bouquets+=1
                    count=0
            else:
                count=0
        return bouquets>=m
    def rose_garden(self, bloom_days, k, m):
        if m*k>len(bloom_days):
            return -1
        low, high=min(bloom_days), max(bloom_days)
        while low<=high:
            mid=(low+high)//2
            if self.is_possible(bloom_days, mid, m, k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    
if __name__=="__main__":
    sol=Solution()
    bloom_days=[7, 7, 7, 7, 13, 11, 12, 7]
    k=3
    m=2
    ans=sol.rose_garden(bloom_days, k, m)
    print(f"We can make bouquets on day {ans}")