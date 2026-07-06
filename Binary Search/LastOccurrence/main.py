class Solution:
    def last_occurrence(self, arr, target):
        low, high=0, len(arr)-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                ans=mid
                low=mid+1
            elif target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        return ans

if __name__=="__main__":
    sol=Solution()
    arr=[3, 4, 4, 4, 7, 8, 10]
    target=4
    ind=sol.last_occurrence(arr, target)
    print(f"The last occurrence of element {target} is: {ind}")