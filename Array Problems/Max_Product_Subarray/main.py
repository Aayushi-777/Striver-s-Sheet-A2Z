class Solution:
    def max_product_subarray(self, arr):
        n=len(arr)
        pre, suff=1, 1
        ans=float("-inf")
        for i in range(n):
            if pre==0:
                pre=1
            if suff==0:
                suff=1
            pre*=arr[i]
            suff*=arr[n-i-1]
            ans=max(ans, pre, suff)
        return ans

if __name__=="__main__":
    sol=Solution()
    arr=[2, 3, -2, 4]
    ans=sol.max_product_subarray(arr)
    print(ans)