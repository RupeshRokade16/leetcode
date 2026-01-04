class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        I need the starting position of all rotten mangos at t=0


        """
        
        q = deque()
        time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:
            
            #process the current q at time i.e the current level
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows)
                        and col in range(cols)
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1 
    