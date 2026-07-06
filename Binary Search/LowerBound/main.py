class Solution:
    def lower_bound(self, arr, x):
        n=len(arr)
        low, high=0, n-1
        ans=len(arr)
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

if __name__=="__main__":
    sol=Solution()
    arr=[3, 5, 8, 15, 19]
    x=9
    ans=sol.lower_bound(arr, x)
    print(f"The lower bound is the index: {ans}")