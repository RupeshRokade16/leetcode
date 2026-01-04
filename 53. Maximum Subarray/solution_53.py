class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        currSum = 0

        i = 0

        while i < len(nums):
            currSum += nums[i]
            
            if currSum > res:
                res = currSum
            
            if currSum < 0:
                currSum = 0
            
            i += 1

        return res
