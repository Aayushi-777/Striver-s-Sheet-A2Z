class Solution:
    def minimum_value(self, arr):
        low, high=0, len(arr)-1
        while low<high:
            mid=(low+high)//2
            if arr[mid]>arr[high]:
                low=mid+1
            else:
                high=mid
        return arr[low]
    
if __name__=="__main__":
    sol=Solution()
    arr=[4,5,6,7,0,1,2]
    ans=sol.minimum_value(arr)
    print(f"The minimum value is: {ans}")