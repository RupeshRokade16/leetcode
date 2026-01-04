class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Circular list

        [1, 2, 3, 1, 6]
        Rob till 1st house -> max(1, 0) -> 1
        Rob till 2nd house -> max(house[0], house[1]) -> 2
        Rob till 3rd house -> max(robtill1st + house[2], robtill2nd) -> 1 + 3, 2 -> 4
        Rob till 4th house -> max(robtill2nd + house[3], robtill3rd) -> 2+1, 3
        Rob till 5th house -> max(4 + 6, 3) -> 10
        But answer should be 9

        [1, 2, 1, 1]
        robtill3rd = 2 + 1 or  

        Solution: Call house robber on 1: & :-1
        """

        def helper(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
