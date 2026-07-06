class Solution:
    def next_greater_element(self, arr):
        n=len(arr)
        ans=[-1]*n
        for i in range(n):
            curr=arr[i]
            for j in range(i+1, n):
                if arr[j]>curr:
                    ans[i]=arr[j]
                    break
        return ans

if __name__=="__main__":
    sol=Solution()
    n=4
    arr=[1, 3, 2, 4]
    ans=sol.next_greater_element(arr)
    print("The next greate elements are: ")
    for i in range(n):
        print(ans[i], end=" ")