class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        

        """
        nums.sort()
        res = []

        def dfs(i, array):
            
            if i >= len(nums):
                res.append(array.copy())
                return

            array.append(nums[i])
            dfs(i+1, array)
            array.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, array)

        dfs(0, [])
        return res
