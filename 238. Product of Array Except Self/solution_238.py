class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        To solve this in constant time, the trick is to
        build a left and right product array for each element in the list
        Left product array -> Product of items to the left of the current number
        Right product array -> Product of items to the right of the current number

        We build the first array as we go from L to R
        and the next one by going R to L
        """
        product_left = [1] * len(nums)
        product_right = [1] * len(nums)

        for idx,num in enumerate(nums):
            if idx!=0:
                product_left[idx] = product_left[idx-1] * nums[idx-1]

        for idx in range(len(nums)-1, -1, -1):
            if idx!=len(nums)-1:
                product_right[idx] = product_right[idx+1] * nums[idx+1]

        res = []
        for i in range(len(nums)):
            res.append(product_left[i] * product_right[i])
        return res
