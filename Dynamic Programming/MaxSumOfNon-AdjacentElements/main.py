class Solution:
    def max_non_adjacent_sum(self, arr):
        n=len(arr)
        if n==1:
            return arr[0]
        dp=[0]*n
        dp[0]=arr[0]
        dp[1]=max(arr[0], arr[1])
        for i in range(2, n):
            dp[i]=max(arr[i]+dp[i-2], dp[i-1])
        return dp[n-1]

if __name__=="__main__":
    sol=Solution()
    arr=[2, 1, 4, 9]
    max_sum=sol.max_non_adjacent_sum(arr)
    print(f"The maximum sum of non-adjacent elements is: {max_sum}")