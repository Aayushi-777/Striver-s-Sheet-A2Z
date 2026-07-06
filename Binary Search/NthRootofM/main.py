class Solution:
    def nth_root(self, n, m):
        low, high=0, m
        nth_root=0
        while low<=high:
            mid=(low+high)//2
            if mid**n==m:
                return mid
            elif mid**n<m:
                low=mid+1
            else:
                high=mid-1
        return -1

if __name__=="__main__":
    sol=Solution()
    n=3
    m=28
    nth_root=sol.nth_root(n, m)
    print(f"The root of {m} is: {nth_root}")