class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        ROWS,COLS = len(board),len(board[0])
        def dfs(r,c):
            if r in range(ROWS) and c in range(COLS) and board[r][c] == "O" and (r,c) not in visit:
                board[r][c] = "T"
                visit.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            else:
                return
        # now i have to run this on the edges of the board
        for r in range(ROWS):
            if board[r][0] == "O" and (r,0) not in visit:
                dfs(r,0)
            if board[r][COLS-1] == "O" and (r,COLS-1) not in visit:
                dfs(r,COLS-1)
        for c in range(COLS):
            if board[0][c] == "O" and (0,c) not in visit:
                dfs(0,c)
            if board[ROWS-1][c] == "O" and (ROWS-1,c) not in visit:
                dfs(ROWS-1,c)
        #now convert all the T to O and O to x
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                    
