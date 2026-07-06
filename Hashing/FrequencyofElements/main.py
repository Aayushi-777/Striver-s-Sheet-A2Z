class Solution:
    def frequencyofelements(self, arr, n):
        visited=[False]*n
        for i in range(n):
            if visited[i]:
                continue
            count=1
            for j in range(i+1, n):
                if arr[i]==arr[j]:
                    visited[j]=True
                    count+=1
            print(arr[i], count)

if __name__=="__main__":
    sol=Solution()
    arr=[10, 5, 15, 10, 5, 10]
    n=len(arr)
    sol.frequencyofelements(arr, n)