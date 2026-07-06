class Solution:
    def rotate_matrix(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        for i in range(n):
            print(matrix[i])
if __name__=="__main__":
    sol=Solution()
    matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    print(f"After rotating the matrix 90 degrees:")
    rotated_mat=sol.rotate_matrix(matrix)
    