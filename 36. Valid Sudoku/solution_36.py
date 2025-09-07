class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        First step was to traverse the entire array. That can be done using 2 for loops
        Next I extracted the current number into a variable and thought about how I would
        be adding it to my hashmaps after checking against a condition.
        Then wrote how it would be added to my hashmap, which gave my a good idea about
        how my hashmaps keys would look like
        Then I wrote the preceding condition which checks the number for the 3 conditions
        and returns false if already present
        Also wrote a small line before this condition to skip any curr_num == '.'
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr_num = board[r][c]
                if curr_num == '.': continue
                if (curr_num in rows[r]) or (curr_num in cols[c]) or (curr_num in grid[(r//3,c//3)]):
                    return False

                rows[r].add(curr_num)
                cols[c].add(curr_num)
                grid[(r//3,c//3)].add(curr_num)  

        return True