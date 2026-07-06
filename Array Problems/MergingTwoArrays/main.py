class Solution:
    def merging_arrays(self, arr1, arr2, n, m):
        i=n-1
        j=m-1
        k=m+n-1
        while i>=0 and j>=0:
            if arr1[i]>arr2[j]:
                arr1[k]=arr1[i]
                i-=1
            else:
                arr1[k]=arr2[j]
                j-=1
            k-=1
        while j>=0:
            arr1[k]=arr2[j]
            k-=1
            j-=1
        return arr1

if __name__=="__main__":
    sol=Solution()
    arr1=[1, 3, 5, 0, 0, 0]
    arr2=[2, 4, 6]
    m, n=3, 3
    arr=sol.merging_arrays(arr1, arr2, n, m)
    print(arr)