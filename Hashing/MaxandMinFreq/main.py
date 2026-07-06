class Solution:
    def maxandminfreq(self, arr, n):
        visited=[False]*n
        maxFreq=0
        minFreq=n
        maxEl=0
        minEl=0
        for i in range(n):
            if visited[i]:
                continue
            count=1
            for j in range(i+1, n):
                if arr[i]==arr[j]:
                    visited[j]=True
                    count+=1
            if count>maxFreq:
                maxEl=arr[i]
                maxFreq=count
            if count<minFreq:
                minEl=arr[i]
                minFreq=count
        print(f"The highest frequency element is: {maxEl}")
        print(f"The lowest frequency element is: {minEl}")
if __name__=="__main__":
    sol=Solution()
    arr=[1,2,3,1,5,5,6,5,6,3,2,7]
    n=len(arr)
    sol.maxandminfreq(arr, n)
