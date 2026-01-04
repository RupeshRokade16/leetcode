class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            
            #mark as visited
            grid[r][c] = 2

            neighbors_area = 0
            for dr, dc in directions:
                neighbors_area += dfs(r + dr, c + dc)

            return neighbors_area + 1
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
