class Solution:
    def missing_kth_value(self, arr, k):
        low, high=0, len(arr)-1
        while low<=high:
            mid=(low+high)//2
            miss_cnt=arr[mid]-(mid+1)
            if miss_cnt<k:
                low=mid+1
            else:
                high=mid-1
        return low+k
    
if __name__=="__main__":
    sol=Solution()
    arr=[4, 7, 9, 10]
    k=4
    missing=sol.missing_kth_value(arr, k)
    print("The missing value is:",missing)