class Solution:
    def count_subsets_sum_k(self, arr, k):
        n=len(arr)
        dp=[[0]*(k+1) for i in range(n)]
        dp[0][0]=1
        if arr[0]<=k:
            dp[0][arr[0]]=1
        for ind in range(1, n):
            for target in range(k+1):
                not_taken=dp[ind-1][target]
                taken=0
                if arr[ind]<=target:
                    taken=dp[ind-1][target-arr[ind]]
                dp[ind][target]=taken+not_taken
        return dp[n-1][k]

if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3, 3]
    k=6
    ans=sol.count_subsets_sum_k(arr, k)
    print(ans) 