class Solution:
    def is_sorted(self, arr):
        n=len(arr)
        for i in range(1, n):
            if arr[i]<arr[i-1]:
                return False
        return True
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    result=sol.is_sorted(arr)
    print(f"The array is sorted: {result}")
