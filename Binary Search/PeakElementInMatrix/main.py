class Solution:
    def max_el(self, arr, col):
        n=len(arr)
        max_val=float('-inf')
        index=-1
        for i in range(n):
            if arr[i][col]>max_val:
                max_val=arr[i][col]
                index=i
        return index
    def find_peak_grid(self, mat):
        n, m=len(mat), len(mat[0])
        low, high=0, m-1
        while low<=high:
            mid=(low+high)//2
            row=self.max_el(mat, mid)
            left=mat[row][mid-1] if mid-1>=0 else float('-inf')
            right=mat[row][mid+1] if mid+1<m else float('-inf')
            if mat[row][mid]>left and mat[row][mid]>right:
                return [row, mid]
            elif left>mat[row][mid]:
                high=mid-1
            else:
                low=mid+1
        return [-1, -1]

if __name__=="__main__":
    sol=Solution()
    mat=[[1, 2, 3], [6, 5, 4], [7, 8, 9]]
peak=sol.find_peak_grid(mat)
print(f"The peak element in the matrix is at: {peak}")