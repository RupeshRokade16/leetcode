class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Watched the soln, not really intuitive, but here's my understanding:

        we call dfs at each index
        then define the a window from index to end of string (for j in range(i, len(s)))

        then we check if this string s[i: j+1] is a palindrome
        if yes, 
            we add it to the partition,
            check dfs for further index, i.e j+1
            then pop that addition and continue (to expand current partition)
        if not, j will incremement to consider a new search window
        
        """


        res = []
        partition = []

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):

            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):  #for remaining string
                if isPali(s, i, j):
                    partition.append(s[i: j+1])
                    dfs(j + 1)
                    partition.pop()

        dfs(0)
        return res
