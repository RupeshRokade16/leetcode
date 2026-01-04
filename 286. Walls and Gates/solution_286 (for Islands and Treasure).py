class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        For traversable spot,
        find if it can move to some spot

        if it is blocked off on all 4 sides, skip that number
        Like dp, leverage the min of the steps needed from all traversible options

        if I start from all 0s and spread in spreadable directions,
        then I can extend the nearest positions at the same time
        if grid[r][c] is not -1 and not 0, I can mark it as min of current, new computation


        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def addRoom(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                (r,c) in visited or grid[r][c] == -1):
                return 

            visited.add((r,c))
            queue.append((r,c))

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r, c))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist

                #This can be wrapped into a fn like addRoom(r, c)
                # for dr, dc in directions:
                #     row, col = r + dr, c + dc
                #     if (row < 0 or col < 0 or row < rows or col < cols or 
                #         (row, col) in visited or grid[row][col] == -1):
                #         return 

                #     visited.append((row, col))
                #     queue.append((row, col))

                addRoom(r + 1, c)
                addRoom(r, c + 1)
                addRoom(r - 1, c)
                addRoom(r, c - 1)

            dist += 1
