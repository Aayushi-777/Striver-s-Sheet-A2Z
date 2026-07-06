class Solution:
    def largestelement(self, arr):
        n=len(arr)
        largest=arr[0]
        for i in range(1, n):
            if arr[i]>largest:
                largest=arr[i]
        print(f"The largest element is: {largest}")
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    sol.largestelement(arr)