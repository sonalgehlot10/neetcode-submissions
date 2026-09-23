class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr,nc = row + dr, col + dc
                    if (nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            time += 1
        
        return time if fresh == 0 else -1
                