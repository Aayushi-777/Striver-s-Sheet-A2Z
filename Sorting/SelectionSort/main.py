class Solution:
    def selection_sort(self, arr):
        n=len(arr)
        for i in range(n-1):
            min_index=i
            for j in range(i+1, n):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[i], arr[min_index]=arr[min_index], arr[i]
        print("After selection sort:")
        print(*arr)
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    sol.selection_sort(arr)

# Time Complexity: O(N^2)
# Space Complexity: O(1)