class Solution:
    def single_non_duplicate(self, arr):
        n=len(arr)
        if n==1:
            return arr[0]
        if arr[0]!=arr[1]:
            return arr[0]
        elif arr[n-1]!=arr[n-2]:
            return arr[n-1]
        low, high=0, n-2
        while low<=high:
            mid=(low+high)//2
            if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
                return arr[mid]
            if (mid%2==1 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid+1]):
                low=mid+1
            else:
                high=mid-1
        return -1

if __name__=="__main__":
    sol=Solution()
    arr=[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    ans=sol.single_non_duplicate(arr)
    print("The single non-duplicate element is:", ans)