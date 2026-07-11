class Solution:
    def min_platforms(self, arr, dep):
        arr.sort()
        dep.sort()
        n=len(arr)
        i, j=1, 0
        result=1
        platforms=1
        while i<n and j<n:
            if arr[i]<=dep[j]:
                platforms+=1
                i+=1
            else:
                platforms-=1
                j+=1
            result=max(result, platforms)
        return result
    
if __name__=="__main__":
    sol=Solution()
    arr=[900, 945, 955, 1100, 1500, 1800]
    dep=[920, 1200, 1130, 1150, 1900, 2000]
    res=sol.min_platforms(arr, dep)
    print(f"Minimum platforms needed: {res}")
