class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def safe(r,c):
            #CORNER 'O' SO CAN'T BE SURROUNDED
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O'):
                return
            board[r][c] = 'S'
            safe(r+1, c)
            safe(r-1, c)
            safe(r, c+1)
            safe(r, c-1)

        for c in range(COLS):
            safe(0, c)
            safe(ROWS-1, c)

        for r in range(ROWS):
            safe(r, 0)
            safe(r, COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
        