class Solution:
    def can_partition(sef, arr):
        n=len(arr)
        total_sum=sum(arr)
        if total_sum%2!=0:
            return False
        target=total_sum//2
        dp=[[False]*(target+1) for i in range(n)]
        for i in range(n):
            dp[i][0]=True
        if arr[0]<=target:
            dp[0][arr[0]]=True
        for ind in range(1, n):
            for tar in range(target+1):
                not_taken=dp[ind-1][tar]
                taken=False
                if arr[ind]<=tar:
                    taken=dp[ind-1][tar-arr[ind]]
                dp[ind][tar]=not_taken or taken
        return dp[n-1][target]
    
if __name__=="__main__":
    sol=Solution()
    arr=[2, 3, 3, 3, 4, 5]
    ans=sol.can_partition(arr)
    if ans:
        print(f"The array can be partitioned to give equal sum.")
    else:
        print(f"The arrar cannot be partitioned to give equal sum.")