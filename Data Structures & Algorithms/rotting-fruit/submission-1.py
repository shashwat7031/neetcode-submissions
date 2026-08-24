class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        time = 0
        fresh = 0
        visit = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
        while q and fresh > 0:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr,dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(ROWS) and c in range(COLS) and (r,c) not in visit and grid[r][c] == 1:
                        fresh -=1
                        q.append((r,c))
                        visit.add((r,c))
            time +=1
        if fresh == 0 :
            return time
        else:
            return -1