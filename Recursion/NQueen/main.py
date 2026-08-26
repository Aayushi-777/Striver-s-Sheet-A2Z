class Solution:
    def solve(self, col, board, n, leftRow, upperDiagonal, lowerDiagonal, ans):
        if col==n:
            ans.append(["".join(row) for row in board])
            return
        for row in range(n):
            if(leftRow[row]==0 and lowerDiagonal[row+col]==0 and upperDiagonal[n-1+col-row]==0):
                board[row][col]='Q'
                leftRow[row]=1
                lowerDiagonal[row+col]=1
                upperDiagonal[n-1+col-row]=1
                self.solve(col+1, board, n, leftRow, upperDiagonal, lowerDiagonal, ans)
                board[row][col]='.'
                leftRow[row]=0
                lowerDiagonal[row+col]=0
                upperDiagonal[n-1+col-row]=0
    def solve_N_queens(self, n):
        ans=[]
        board=[['.' for _ in range(n)] for _ in range(n)]
        leftRow=[0]*n
        upperDiagonal=[0]*(2*n-1)
        lowerDiagonal=[0]*(2*n-1)
        self.solve(0, board, n, leftRow, upperDiagonal, lowerDiagonal, ans)
        return ans

if __name__=="__main__":
    sol=Solution()
    n=7
    res=sol.solve_N_queens(n)
    for board in res:
        for row in board:
            print(row)
        print()
