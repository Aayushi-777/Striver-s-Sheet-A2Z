class Solution:
    def merge(self, arr, low, mid, high):
        temp=[]
        left, right=low, mid+1
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right+=1
        for i in range(low, high+1):
            arr[i]=temp[i-low]
    def merge_sort(self, arr, low, high):
        if low>=high:
            return
        mid=(low+high)//2
        self.merge_sort(arr, low, mid)
        self.merge_sort(arr, mid+1, high)
        self.merge(arr, low, mid, high)
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    sol.merge_sort(arr, 0, len(arr)-1)
    print("After merge sort:")
    print(*arr)

# Time Complexity: O(N*logN)
# Space Complexity: O(N)