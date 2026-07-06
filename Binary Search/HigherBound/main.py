class Solution:
    def upper_bound(self, arr, x):
        n=len(arr)
        ans=len(arr)
        low, high=0, n-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

if __name__=="__main__":
    sol=Solution()
    arr=[3, 5, 8, 9, 15, 19]
    x=9
    ans=sol.upper_bound(arr, x)
    print(f"The upper bound is the index: {ans}")