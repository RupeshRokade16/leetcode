class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr = xorr ^ i ^ nums[i]
        return xorr

    """XOR properties
    a XOR a = 0 (also written as a ^ a = 0)
    a ^ 0 = a

    All common numbers cancel out. 
    Example 2
    Iteration 1:
    xorr = 2
    2 ^ 0 ^ 0 = 2

    Iteration 2:
    xorr = 2
    2 ^ 1 ^ 2 = 2 ^ 2 ^ 1 = 0 ^ 1 = 1
    """
