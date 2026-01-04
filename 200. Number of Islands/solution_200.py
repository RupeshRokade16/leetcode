class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j, visited):

            if (i, j) in visited or i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] == "0" :
                return

            #valid point
            movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited.add((i, j))

            for di, dj in movements:
                dfs(i + di, j + dj, visited)
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    dfs(i, j, visited)
        return count

"""Alternate way of writing this solution where you dont use visited set

    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return

            grid[r][c] = "0" #mark it as visited
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands
    """
