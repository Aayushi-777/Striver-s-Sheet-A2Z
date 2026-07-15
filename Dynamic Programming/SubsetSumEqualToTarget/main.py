class Solution:
    def subset_sum_k(self, n, k, arr):
        dp=[[False]*(k+1) for i in range(n)]
        for i in range(n):
            dp[i][0]=True
        if arr[0]<=k:
            dp[0][arr[0]]=True
        for ind in range(1, n):
            for target in range(1, k+1):
                not_taken=dp[ind-1][target]
                taken=False
                if arr[ind]<=target:
                    taken=dp[ind-1][target-arr[ind]]
                dp[ind][target]=not_taken or taken
        return dp[n-1][k]
    
if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3, 4]
    k=4
    n=len(arr)
    ans=sol.subset_sum_k(n, k, arr)
    if ans:
        print("The target sum can be formed using the array.")
    else:
        print("The target sum cannot be formed using the array.")