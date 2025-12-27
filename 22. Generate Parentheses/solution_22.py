class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        At each decision point, I either choose to add an opened bracket 
        or a closed bracket (cant choose to not add like general backtracking ones
        since here the positions will be occupied by either an open or a closed 
        bracket regardless)

        I also keep an opened count and a closed count

        At the start of my dfs, I check if we have the right soln, 
        i.e opened == closed == n and add it to res

        I also prune any cases where
            - i overshot
            - len(string) overshot
            - closed > opened

        T: O(4^n/ root of n)

        Can make it faster by using lists and then doing a "".join(list) at the end
        slicing from a list is an O(n) operation

        Remember that I also have to pop at the end, where I add the closed bracket
        """
        res = []

        def dfs(i, opened, closed, array):
            
            #Check for valid res
            
            if opened == closed == n:
                res.append("".join(array))
                return

            #Prune branches that overshot or are invalid
            if i > 2 * n or len(array) > 2 * n or closed > opened:
                return

            #Add open bracket, compute and pop
            if opened < n:
                array.append("(")
                dfs(i + 1, opened + 1, closed, array)
                array.pop()

            #Add closed bracket only if valid
            if closed < n:
                array.append(")")
                dfs(i + 1, opened, closed + 1, array)
                array.pop()

        dfs(0, 0, 0, [])
        return res
