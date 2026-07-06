class Solution:
    def peak_element(self, arr):
        low, high=0, len(arr)-1
        while low<high:
            mid=(low+high)//2
            if arr[mid]>arr[mid+1]:
                high=mid
            else:
                low=mid+1
        return low
    
if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 1, 3, 5, 6, 4]
    peak=sol.peak_element(arr)
    print(f"The peak element is at index: {peak}")