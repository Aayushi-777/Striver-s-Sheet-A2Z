from typing import List
class Solution:
    def is_valid(self, board, row, col, num):
        for j in range(9):
            if board[row][j]==num:
                return False
        for i in range(9):
            if board[i][col]==num:
                return False
        start_row=(row//3)*3
        start_col=(col//3)*3
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                if board[i][j]==num:
                    return False
        return True
    def solve_sudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for num in "123456789":
                        if self.is_valid(board, i, j, num):
                            board[i][j]=num
                            if self.solve_sudoku(board):
                                return True
                            board[i][j]='.'
                    return False
        return True

if __name__=="__main__":
    sol=Solution()
    board=[
        ['9','5','7','.','1','3','.','8','4'],
        ['4','8','3','.','5','7','1','.','6'],
        ['.','1','2','.','4','9','5','3','7'],
        ['1','7','.','3','.','4','9','.','2'],
        ['5','.','4','9','7','.','3','6','.'],
        ['3','.','9','5','.','8','7','.','1'],
        ['8','4','5','7','9','.','6','1','3'],
        ['.','9','1','.','3','6','.','7','5'],
        ['7','.','6','1','8','5','4','.','9']
    ]
    sol.solve_sudoku(board)
    for row in board:
        print(" ".join(row))