class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])  

        def is_valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(i, r, c, visited):
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            visited[r][c] = True
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and not visited[nr][nc]:
                    if dfs(i + 1, nr, nc, visited):
                        return True

            visited[r][c] = False  # backtrack
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
                    if dfs(0, r, c, visited):
                        return True

        return False
