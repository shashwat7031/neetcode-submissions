class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        islands = 0
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                r,c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row in range(ROWS) and col in range(COLS) and grid[row][col] == '1' and (row,col) not in visit):
                        q.append((row,col))
                        visit.add((row,col))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands
            