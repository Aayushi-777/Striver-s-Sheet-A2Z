class Solution:
    def floor_ceiling(self, arr, x):
        floor=0
        ceiling=0
        low, high=0, len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ceiling=arr[mid]
                high=mid-1
            else:
                low=mid+1
        low, high=0, len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<=x:
                floor=arr[mid]
                low=mid+1
            else:
                high=mid-1
        return floor, ceiling

if __name__=="__main__":
    sol=Solution()
    arr=[3, 4, 4, 7, 8, 10]
    x=5
    f, c=sol.floor_ceiling(arr, x)
    print(f"The floor and ceiling of {x} respectively are:", f, c)

        