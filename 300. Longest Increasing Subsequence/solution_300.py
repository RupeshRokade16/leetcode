class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        R to L

        LIS[end] = 1
        LIS[end - 1] = max(LIS[end-1], 1 + LIS[end]) (Only if nums[end - 1] < nums[end])
        LIS[end - 2] = max(LIS[end-2], 1 + LIS[end - 1], 1 + LIS[end - 2])
        LIS[end - 3] = max(LIS[end-3] ,1 + LIS[end-2], 1 + LIS[end - 1], 1 + LIS[end - 2])

        T: O(n^2)

        There is an O(nlogn) solution that uses dynamic programming, study and
        implement it
        """

        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
