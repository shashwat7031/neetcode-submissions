class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        area = 0
        visit = set()
        def bfs(r,c):
            if (r<0 or r == ROWS or c<0 or c == COLS or (r,c) in visit or grid[r][c] == 0):
                return 0 
            visit.add((r,c))
            return (1 + bfs(r+1,c) + bfs(r-1,c) + bfs(r,c+1) + bfs(r,c-1))
        for rows in range(ROWS):
            for cols in range(COLS):
                area = max(area,bfs(rows,cols))
        return area
                