class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid),len(grid[0])
        q = deque()
        visit = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                grid[row][col] = dist
                for dr,dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(ROWS) and c in range(COLS) and (r,c) not in visit and grid[r][c] != -1:
                        q.append((r,c))
                        visit.add((r,c))
            dist +=1
