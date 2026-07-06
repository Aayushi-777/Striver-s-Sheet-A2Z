class Solution:
    def find_pge(self, arr):
        n=len(arr)
        stack=[]
        ans=[0]*n
        for i in range(n):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            ans[i]=-1 if not stack else stack[-1]
            stack.append(i)
        return ans
    def stock_span(self, arr, n):
        pge=self.find_pge(arr)
        ans=[0]*n
        for i in range(n):
            ans[i]=i-pge[i]
        return ans

if __name__=="__main__":
    sol=Solution()
    arr=[120, 100, 60, 80, 90, 110, 115]
    n=7
    ans=sol.stock_span(arr, n)
    print("The span of stack prices is:")
    print(*ans)