class Solution:
    def rec_bubble_sort(self, arr, n):
        if n==1:
            return
        did_swap=False
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                did_swap=True
        if not did_swap:
            return
        self.rec_bubble_sort(arr, n-1)
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    n=len(arr)
    sol.rec_bubble_sort(arr, n)
    print("After recursive bubble sort:")
    print(*arr)

# Time Complexity: O(N^2)
# Space Complexity: O(N)