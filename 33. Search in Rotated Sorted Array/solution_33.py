class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [3, 4, 5, 6, 1, 2] target = 1
        [3, 5, 6, 0, 1, 2] target = 4
            ^ 
        [3, 0, 1, 2, 3, 5] target = 4
            ^
        [4, 5, 6, 7, 0, 1, 2] target = 0
                  ^     ^
        We have to return -1 if not present

        midval = 6
        check left, and compare w target. That becomes the search space
        else check right and compare w target

        How do I confidently exit and return -1 for cases where target not present?
        - What if I write the search in such a way that it exits out if search
        fails eventually (after having moved correctly)

        too many variables for movement
        Comparing mid val against leftmost and rightmost [the right place to start]
        comparing target against leftmost and rightmost

        Check left to mid is sorted,
            then if target is less than mid or mid < target
                Move right
            else
                Move left
        else (mid to right is sorted)
            then if target is greated than right or target < mid
                Move left
            else
                move right

        Imagine the number line for these if statements and it'll make sense
        The binary search will auto exit if number not present (by l crossing over
        r)
        """

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r)//2
            curr = nums[mid]

            if curr == target:
                return mid

            #if left half is sorted
            if nums[l] <= nums[mid]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: #right half is sorted
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
