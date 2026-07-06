class Solution:
    def number_of_rotations(self, arr):
        low, high=0, len(arr)-1
        while low<high:
            mid=(low+high)//2
            if arr[mid]>arr[high]:
                low=mid+1
            else:
                high=mid
        return low
    
if __name__=="__main__":
    sol=Solution()
    arr=[4,5,6,7,0,1,2,3]
    ans=sol.number_of_rotations(arr)
    print(f"The number of rotations are: {ans}")
