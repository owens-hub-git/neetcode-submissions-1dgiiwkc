class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands_seen = set()
        max_area = 0

        def search_island(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0
            if grid[r][c] == 0 or (r, c) in islands_seen:
                return 0
            
            islands_seen.add((r, c))

            return (1 + search_island(r + 1, c) + search_island(r - 1, c) + search_island(r, c + 1) + search_island(r, c - 1))
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in islands_seen and grid[r][c] != 0:
                    max_area = max(max_area, search_island(r,c))
        return max_area