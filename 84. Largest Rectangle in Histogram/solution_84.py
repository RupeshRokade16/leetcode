class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """This is a core pattern to learn
        Check LC 84 and 85, that uses a variation of this technique to solve
        the problem
        
        What's the core ideology to solve such a problem?
            7 1 7 2 2 4

            ^
            Initially max = 7
            Then you go to 1
            Since (curr) 1 < 7 (stacktop)
            you're constraint becomes 1
            So you compute res with min(2 heights) * width
            next you encounter a 7, bigger than old min
                compute res with min height * width
            Next you take 2, we want constraint height to be 2 this time
            How do you do that?

            How can you foretell that you have to drop constraint of 1, what if the 
            array is 7 1 7 2 2 4 and a thousand 1s? Also when can we confidently
            drop the first 7 that we had encountered?

            - Should we use length of the remaining array for such calculation?

            For 7, 1 we can extend 1 Left and Right, but we can surely not extend
            7 rightwards
            If it were 1, 7. We could extend 1 rightwards as well as 7 rightwards
            What if they were the same?
            7, 7 (Then we can keep extending them)

            So we want to calculate the heights that are in increasing order
            When they arent, 
                they will be popped

            1, 2, 3, 4, 3
            ^               can be extended to the right
               ^            can be extended to the right
                  ^         can be extended to the right
                     ^      can be extended to the right    
                        ^   Now the 4 cant be extended to the right any further

                            Then we can compute 4s answer and pop it 

                            if we had introduced a 2 (instead of 3), then we would have 
                            computed 4's area to the right (4), popped 4, 
                            computed 3's area to the right (6), popped 3

        So we are popping latest (therefore a stack)
        and we are keeping the stack monotonically increasing
        Its called monotonically increasing stack

        What goes in the stack as an element? 
        (index, height)
        For input = [2, 1, 5]
        stack = [(0, 2)]
        stack = [(0, 2)] (1, 1) (since 1 < 2) compute res, 2 * 1 = 2, pop
                and add (1, 1) but change its index to 0 since it couldve been extended
                to the left
                [(0, 1)]
        stack = [(0, 1), (2, 5)] 

        Then pop the stack to compute res? - Yes, and use the starting indices for that height to compute
        the area (which will extend till the end of the array)
                        
        """

        stack = []          #holds (starting index for a specific height, height)
        res = 0

        for i, height in enumerate(heights):
            start = i

            #curr num is smaller, pop and compute res
            while stack and height < stack[-1][1]:
                last_idx, last_height = stack.pop()

                area = (i - last_idx) * last_height     #popped height was valid for a width == current width
                if area > res:  res = area
                res = max(res, area)

                start = last_idx    #update to let new height be appended with this index
                
            stack.append((start, height))       #adds the number if stack empty, if valid or using the new
                                                #computed index for the current height (from the while loop)

        for i, height in stack:
            res = max(res, height * (len(heights) - i))

        return res
