class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def valid_row(board):
            for i in range(9):
                seen = set()
                for j in range(9):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True

        def valid_col(board):
            for j in range(9):
                seen = set()
                for i in range(9):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True

        def valid_box(board):
            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    seen = set()
                    for i in range(row, row + 3):
                        for j in range(col, col + 3):
                            if board[i][j] == ".":
                                continue
                            if board[i][j] in seen:
                                return False
                            seen.add(board[i][j])
            return True

        return valid_row(board) and valid_col(board) and valid_box(board)