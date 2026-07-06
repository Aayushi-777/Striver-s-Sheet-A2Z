class Solution:
    def secondlargestandsmallest(self, arr):
        n=len(arr)
        if n==0 or n==1:
            print(-1, -1)
            return
        small=float('inf')
        sec_small=float('inf')
        large=float('-inf')
        sec_large=float('-inf')
        for i in range(n):
            small=min(arr[i], small)
            large=max(arr[i], large)
        for i in range(n):
            if arr[i]<sec_small and arr[i]!=small:
                sec_small=arr[i]
            if arr[i]>sec_large and arr[i]!=large:
                sec_large=arr[i]
        print(f"Second smallest element is: {sec_small}")
        print(f"Second largest element is: {sec_large}")
if __name__=="__main__":
    sol=Solution()
    arr=[5, 10, 65, 75, 45, 35, 67]
    sol.secondlargestandsmallest(arr)
