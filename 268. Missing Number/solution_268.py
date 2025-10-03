class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        desired_sum = 0
        for i in range(0, n+1):
            desired_sum += i
        
        return desired_sum - sum(nums)