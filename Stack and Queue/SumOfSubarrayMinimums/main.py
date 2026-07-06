class Solution:
    def find_nse(self, arr):
        n=len(arr)
        ans=[0]*n
        stack=[]
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            else:
                ans[i]=n
            stack.append(i)
        return ans
    def find_psee(self, arr):
        n=len(arr)
        ans=[0]*n
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            else:
                ans[i]=-1
            stack.append(i)
        return ans
    def sum_subarray_min(self, arr):
        nse=self.find_nse(arr)
        psee=self.find_psee(arr)
        mod=10**9+7
        total=0
        for i in range(len(arr)):
            left=i-psee[i]
            right=nse[i]-i
            total=(total+arr[i]*left*right)%mod
        return total

if __name__=="__main__":
    sol=Solution()
    arr=[3, 1, 2, 5]
    ans=sol.sum_subarray_min(arr)
    print(f"Sum of Subarray Minimums: {ans}")