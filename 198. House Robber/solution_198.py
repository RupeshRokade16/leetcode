class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: 
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        """
        For nums = [2, 7, 9, 3, 1] 
        reach1st = nums[0] -> 2
        reach2nd = max(nums[0], nums[1]) -> 7
        reach3rd = max(reach1st + nums[2], reach2nd) -> 2+9, 7 -> 11
        reach4th = max(reach2nd + nums[3], reach3rd) -> 7+3, 11 -> 11
        reach5th = max(reach3rd + nums[4], reach4th) -> 11 + 1, 11 -> 12
        """

        # rob = 0
        # second_last, last = nums[0], max(nums[1], nums[0])
        # for i in range(3, n + 1):
        #     #Reaches n, which is the end of the house, so satisfies our requirement
        #     rob = max(second_last + nums[i - 1], last)
        #     second_last = last
        #     last = rob

        # return rob

        """Cleaner Code"""
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
