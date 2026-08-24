class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid),len(grid[0])
        q = deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        def check(r,c):
            if r in range(ROWS) and c in range(COLS) and grid[r][c] != -1 and (r,c) not in visit:
                q.append((r,c))
                visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                check(r+1,c)
                check(r-1,c)
                check(r,c+1)
                check(r,c-1)
            dist +=1