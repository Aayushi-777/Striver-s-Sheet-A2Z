class Solution:
    def bubble_sort(self, arr):
        n=len(arr)
        for i in range(n-1, -1, -1):
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1]=arr[j+1], arr[j]
        print("After bubble sort:")
        print(*arr)
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    sol.bubble_sort(arr)

# Time Complexity: O(N^2)
# Space Complexity: O(1)