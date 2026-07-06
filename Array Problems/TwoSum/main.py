class Solution:
    #VARIANT 1 TWO SUM EXISTS OR NOT
    def two_sum_exists(self, arr, target):
        n=len(arr)
        seen=set()
        for i in range(n):
            needed=target-arr[i]
            if needed in seen:
                return "YES"
            seen.add(arr[i])
        return "NO"
    
    #VARIANT 2 TWO SUM EXISTS AT WHAT INDEX
    def two_sum_indices(self, arr, target):
        seen={}
        n=len(arr)
        for i in range(n):
            needed=target-arr[i]
            if needed in seen:
                return [seen[needed], i]
            seen[arr[i]]=i
        return [-1, -1]

if __name__=="__main__":
    sol=Solution()
    arr=[2, 6, 5, 8, 11]
    target=14
    print(sol.two_sum_exists(arr, target))
    print(sol.two_sum_indices(arr, target))
