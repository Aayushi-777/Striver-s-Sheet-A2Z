class Solution:
    def count_partitions(self, arr, d):
        n=len(arr)
        total_sum=sum(arr)
        if total_sum<d or (total_sum+d)%2!=0:
            return 0
        target=(total_sum+d)//2
        dp=[[0]*(target+1) for i in range(n)]
        dp[0][0]=1
        if arr[0]<=target:
            dp[0][arr[0]]+=1
        for ind in range(1, n):
            for tar in range(target+1):
                not_taken=dp[ind-1][tar]
                taken=0
                if arr[ind]<=tar:
                    taken=dp[ind-1][tar-arr[ind]]
                dp[ind][tar]=not_taken+taken
        return dp[n-1][target]
    
if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3, 4]
    d=2
    ans=sol.count_partitions(arr, d)
    print(f"Number of partitions with diff {d} are: {ans}")
