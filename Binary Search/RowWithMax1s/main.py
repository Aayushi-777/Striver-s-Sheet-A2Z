class Solution:
    def lower_bound(self, arr, n, x):
        low, high=0, n-1
        ans=n
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def row_with_max_1s(self, matrix, n, m):
        cnt_max=0
        ind=-1
        for i in range(n):
            cnt_ones=m-self.lower_bound(matrix[i], m, 1)
            if cnt_ones>cnt_max:
                cnt_max=cnt_ones
                ind=i
        return ind
    
if __name__=="__main__":
    sol=Solution()
    matrix=[[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    m, n=3, 3
    ind=sol.row_with_max_1s(matrix, n, m)
    print(f"The row with max 1s has index: {ind}")