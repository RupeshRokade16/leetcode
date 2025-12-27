class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        """
        For every number, you choose to include it or not include it

        Which means, during every recursive entry, we pass a list?

        Recursively using dfs and index of the array
        """

        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])   #just subset creates same memory problem
                return


            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)

        return res
