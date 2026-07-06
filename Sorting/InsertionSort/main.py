class Solution:
    def insertion_sort(self, arr):
        n=len(arr)
        for i in range(1, n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        print("After insertion sort:")
        print(*arr)
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    sol.insertion_sort(arr)

# Time Complexity: O(N^2)
# Space Complexity: O(1)