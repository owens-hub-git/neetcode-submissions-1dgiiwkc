class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, set_seen):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == "0":
                return
            if (r, c) in set_seen:
                return
            set_seen.add((r, c))

            dfs(r + 1, c, set_seen)
            dfs(r, c + 1, set_seen)
            dfs(r - 1, c, set_seen)
            dfs(r, c - 1, set_seen) 

        set_seen = set()
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in set_seen and grid[r][c] == "1":

                    dfs(r, c, set_seen)
                    count += 1

        return count