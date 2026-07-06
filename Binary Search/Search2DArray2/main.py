"""
class Solution:
    def search_2D_array(self, matrix, target):
        n, m=len(matrix), len(matrix[0])
        low, high=0, (m*n)-1
        while low<=high:
            mid=(low+high)//2
            row=mid//m
            col=mid%m
            if matrix[row][col]==target:
                return [row, col]
            elif matrix[row][col]>target:
                high=mid-1
            else:
                low=mid+1
        return [-1, -1]

if __name__=="__main__":
    sol=Solution()
    matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    target=9
    ans=sol.search_2D_array(matrix, target)
    print(f"The element {target} is found at index: {ans}")

This works if the 2D array is sorted
"""

class Solution:
    def search_2D_array(self, matrix, target):
        n, m=len(matrix), len(matrix[0])
        row, col=0, m-1
        while row<n and col>=0:
            if matrix[row][col]==target:
                return [row, col]
            elif matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return [-1, -1]

if __name__=="__main__":
    sol=Solution()
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target=9
    ans=sol.search_2D_array(matrix, target)
    print(f"The element {target} is found at index: {ans}")


