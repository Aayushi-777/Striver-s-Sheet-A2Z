class Solution:
    def element_rotated_array(self, arr, x):
        low, high=0, len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                return True
            if arr[low]==arr[mid]==arr[high]:
                low+=1
                high-=1
                continue
            if arr[low]<=arr[mid]:
                if arr[low]<=x<=arr[mid]:
                    high=mid-1
                else:
                    low=mid+1
            if arr[mid]<=arr[high]:
                if arr[mid]<=x<=arr[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False
    
if __name__=="__main__":
    sol=Solution()
    arr=[7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    x=3
    ans=sol.element_rotated_array(arr, x)
    print(f"Is element {x} present in array: {ans}")
