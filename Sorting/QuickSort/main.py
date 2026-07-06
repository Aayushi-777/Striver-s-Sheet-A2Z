class Solution:
    def quick_sort(self, arr, low, high):
        if low<high:
            pivot=self.partition(arr, low, high)
            self.quick_sort(arr, low, pivot-1)
            self.quick_sort(arr, pivot+1, high)
    def partition(self, arr, low, high):
        pivot=arr[high]
        i=low-1
        for j in range(low, high):
            if arr[j]<=pivot:
                i+=1
                arr[i], arr[j]=arr[j], arr[i]
        arr[i+1], arr[high]=arr[high], arr[i+1]
        return i+1
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    n=len(arr)
    sol.quick_sort(arr, 0, n-1)
    print("After quick sort:")
    print(*arr)

# Time Complexity: O(N*logN)
# Space Complexity: O(N)