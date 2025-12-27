class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Search through the array, find the word[0] in the grid

        Then write dfs function which recursively checks if the given path contains
        the solution

        Couldve also written this solution with dfs returning True or False (that 
        wouldve skipped the nonlocal flag)
        """
        rows = len(board)
        cols = len(board[0])

        flag = False

        def dfs(i, j, visited, word_idx):
            nonlocal flag

            if flag: return 
            if board[i][j] != word[word_idx]:
                return
            if word_idx == len(word) - 1:
                flag = True
                return
            
            movements = [(i+1, j), 
            (i, j+1), 
            (i-1, j), 
            (i, j - 1)]

            visited.add((i, j))

            for movement in movements:
                ith, jth = movement
                
                if (((ith, jth) not in visited) and 
                    (0 <= ith < rows) and 
                    (0 <= jth < cols) and 
                    (board[ith][jth] == word[word_idx + 1])):

                    dfs(ith, jth, visited, word_idx + 1)

            visited.discard((i,j))


        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    dfs(i, j, set(), 0)
                    if flag:
                        return True
        return flag
