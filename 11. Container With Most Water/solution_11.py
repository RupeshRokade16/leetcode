class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Order can not be changed here
        We can update max_area variable till we can scan the entire array using a 2ptr approach
        Thinking that we fix the particular ptr with more height to get max area
        
        What if heights are the same?
        Either of the 2 ptrs can be updated, so use just one
        """
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            smaller = min(heights[l], heights[r])
            area = smaller * (r-l)
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
    