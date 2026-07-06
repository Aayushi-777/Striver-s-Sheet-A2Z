class Solution:
    def element_rotated_array(self, arr, x):
        low, high=0, len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                return mid
            if arr[low]<arr[mid]:
                if arr[low]<=x<arr[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if arr[mid]<x<=arr[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1

if __name__=="__main__":
    sol=Solution()
    arr=[4,5,6,7,0,1,2]
    x=0
    ans=sol.element_rotated_array(arr, x)
    print(f"The element {x} is at index: {ans}")
