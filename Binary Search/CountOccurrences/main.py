class Solution:
    def count_occurrences(self, arr, target):
        low, high=0, len(arr)-1
        count=0
        first, last=-1, -1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                first=mid
                high=mid-1
            elif target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        low, high=0, len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                last=mid
                low=mid+1
            elif target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        ans=last-first+1
        return ans

if __name__=="__main__":
    sol=Solution()
    arr=[2, 2, 3, 3, 3, 3, 4]
    target=3
    count=sol.count_occurrences(arr, target)
    print(f"The number of occurrences of element {target} is: {count}")