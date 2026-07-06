class Solution:
    def set_matrix_zero(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        first_row_zero=False
        first_col_zero=False
        for j in range(m):
            if matrix[0][j]==0:
                first_row_zero=True
                break
        for i in range(n):
            if matrix[i][0]==0:
                first_col_zero=True
                break
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if first_row_zero:
            for j in range(m):
                matrix[0][j]=0
        if first_col_zero:
            for i in range(n):
                matrix[i][0]=0
        for row in matrix:
            print(row, end=" ")

if __name__=="__main__":
    sol=Solution()
    matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print("The matrix after setting rows and columns to zero is:")
    sol.set_matrix_zero(matrix)
