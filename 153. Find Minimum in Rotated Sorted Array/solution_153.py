class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Intuition, write binary search to find the highest number in arr
        If highest number in arr has a value to its right index, then that's
        the answer
        If highest number has no value to its right index, then arr[0] is the 
        answer

        [5, 0, 1, 2, 3, 4]
        [3, 4, 5, 6, 1, 2]
        [4, 5, 6, 7, 0, 1, 2]

        I have to use guiding towards of Left and Right to move towards the
        rotation point

        What should my exit condition be? I'm confused whether I should traverse
        to find the highest number in the search space or whether I should find
        the lowest number in the search space

        Writing conditions for landing on both and returning the answer then
        worked

        My solution requires the edge cases written else it doesnt work
        """

        l, r = 0, len(nums) - 1

        #Edge Case - Non rotated array
        if nums[l] < nums[r] or len(nums) == 1:
            return nums[l]
        if len(nums) == 2:
            return min(nums[0], nums[1])

        while l <= r:
            Left, Right = nums[l], nums[r]
            mid = (l + r) // 2
            curr = nums[mid]

            if curr > nums[mid + 1]:
                return nums[mid + 1]
            if curr < nums[mid + 1] and curr < nums[mid - 1]:
                return curr
            
            if curr > Right:
                l = mid + 1
            
            else:
                r = mid - 1


        """
        Neetcode's solution
        
        If left half is sorted, min cant be there, so search right half
        If right half is sorted, min can be at left half or at mid

        l, r = 0, len(nums) - 1
        min = res[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r)//2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res

        """
        
            


