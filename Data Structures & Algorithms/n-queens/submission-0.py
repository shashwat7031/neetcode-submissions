class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        posdiag = set()
        negdiag = set()
        col = set()
        res = []
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return res
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                
                col.add(c)
                posdiag.add(c+r)
                negdiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res
            
            