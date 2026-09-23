class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])
        area = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            res = 1

            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    q.append((nr,nc))
                    res += 1
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        return area

# Time: O(m*n)
# Space: O(m*n)
