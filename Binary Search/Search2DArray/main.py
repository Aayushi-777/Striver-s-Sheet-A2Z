class Solution:
    def search_2d_array(self, matrix, target):
        n, m=len(matrix), len(matrix[0])
        low, high=0, n*m-1
        while low<=high:
            mid=(low+high)//2
            row=mid//m
            col=mid%m
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high=mid+1
            else:
                low=mid-1
        return False
    
if __name__=="__main__":
    sol=Solution()
    matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    target=8
    ans=sol.search_2d_array(matrix, target)
    print(f"Does the element {target} exist in the 2D array?: {ans}")