class Solution:
    def find_nse(self, arr):
        n=len(arr)
        stack=[]
        ans=[0]*n
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            else:
                ans[i]=n
            stack.append(i)
        return ans
    def find_nge(self, arr):
        n=len(arr)
        ans=[0]*n
        stack=[]
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]]<=arr[i]:
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
    def find_pgee(self, arr):
        n=len(arr)
        ans=[0]*n
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]<arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            else:
                ans[i]=-1
            stack.append(i)
        return ans
    def sum_min(self, arr):
        nse=self.find_nse(arr)
        psee=self.find_psee(arr)
        n=len(arr)
        total=0
        for i in range(n):
            left=i-psee[i]
            right=nse[i]-i
            total+=arr[i]*left*right
        return total
    def sum_max(self, arr):
        nge=self.find_nge(arr)
        pgee=self.find_pgee(arr)
        total=0
        n=len(arr)
        for i in range(n):
            left=i-pgee[i]
            right=nge[i]-i
            total+=arr[i]*left*right
        return total
    def sum_subarray_range(self, arr):
        return self.sum_max(arr)-self.sum_min(arr)

if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3]
    ans=sol.sum_subarray_range(arr)
    print(f"The sum of range of subarrays is: {ans}")