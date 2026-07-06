class Solution:
    def binary_search(self, arr, target):
        n=len(arr)
        low, high=0, n-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                return mid
            elif target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1

if __name__=="__main__":
    sol=Solution()
    arr=[3, 4, 6, 7, 9, 12, 16, 17]
    target=6
    ind=sol.binary_search(arr, target)
    if ind==-1:
        print("No element found in the array.")
    else:
        print(f"Element found at index: {ind}")