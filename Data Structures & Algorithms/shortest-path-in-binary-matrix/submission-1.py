class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        q = deque([(0, 0, 1)])
        been_to = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        been_to.add((0,0))

        while q:
            r, c, length = q.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return length

            for row, col in directions:
                new_row, new_col = r + row, c + col
                if ((new_row, new_col) not in been_to and new_row < len(grid) and new_col < len(grid[0]) and new_row >= 0 and new_col >= 0 and grid[new_row][new_col] == 0):
                    been_to.add((new_row, new_col))
                    q.append((new_row, new_col, length + 1))
        
        return -1