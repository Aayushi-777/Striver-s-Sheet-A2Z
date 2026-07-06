class Solution:
    def rec_insertion_sort(self, arr, n):
        if n<=1:
            return
        self.rec_insertion_sort(arr, n-1)
        key=arr[n-1]
        j=n-2
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    n=len(arr)
    sol.rec_insertion_sort(arr, n)
    print("After recursive insertion sort:")
    print(*arr)

# Time Complexity: O(N^2)
# Space Complexity: O(N)