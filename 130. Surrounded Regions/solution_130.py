class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Can I mark an O as X at each step before moving forward with a recursive
        call? 
        Maybe I can store the indices in some temp list, and only append when all 4 
        are surrounded

        1. Base case - Edge or OOB cells return False
        2. Internal adjacent Os are valid, extend recrusive DFS and return True if
        extended DFS returns True, else False (meaning blob of Os are not surrounded)
        3. If adjacent is 1, return True

        Can think of this problem conversely:
        Capture everything except unsurrounded regions
            Find Os on the border, then mark it T and run DFS on those
            The DFS will mark T on all adjacent Os to those positions
            Then after the DFS, loop through and mark all Os as X
            and all Ts back as O

        This converse way is better to think
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        #Extend border Os (O becomes T)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and r in [0, rows - 1] or c in [0, cols - 1]:
                    dfs(r, c)

        #All remaining Os are now capturable
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #All Ts will be flipped back to O (non capturable Os)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                    