class Solution:
    def linear_search(self, arr, num):
        n=len(arr)
        for i in range(n):
            if arr[i]==num:
                return i
        return -1
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    num=55
    index=sol.linear_search(arr, num)
    print(f"The number {num} is at index: {index}")

# Time Complexity: O(N)
# Space Complexity: O(1)