class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Here, position can be interchanged
        In previous questions, we were incrementing i and building our recursive
        soln according to i

        Here, for a case like [0, 1]
        The decision tree starting from [1] wont ever choose 0 because i has been
        incremented

        Maybe a set of indices travelled? But that would make the recrusive traversing hard because want to just do one thing, undo that thing and move to the next thing during each unit movement of a dfs call

        T: O(n! * n^2)
        S: O(n! * n)

        """

        if len(nums) == 0:
            return [[]]       #base case

        perms = self.permute(nums[1:])     # [ [] ] | [3]
        res = []                            
        print(perms)
        for p in perms:                   #[] in [ [] ] | [3] in [ [3] ]
            for i in range(len(p) + 1):   #range = [0,1] | [0:2]
                p_copy = p.copy()         #p_copy = []  | [3]
                p_copy.insert(i, nums[0]) #p_copy = [3] | [2, 3] or [3, 2]
                res.append(p_copy)        #returned to caller, res = [3], res = [2, 3]

        return res


        """Iterative way
        
        perms = [[]]          #base case

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
        
            perms = new_perms #Update the perms for next iterations

        return perms
        
        
        """
