class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        area = 0 
        def bfs(r,c):
            l = 1 
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1 and (row,col) not in visit:
                        l +=1
                        q.append((row,col))
                        visit.add((row,col))
            return l

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area,bfs(r,c))
        return area