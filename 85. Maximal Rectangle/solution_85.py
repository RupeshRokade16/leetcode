class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Say I was calling dfs, it needs to be well controlled such that it computes
        a possible res when the path is valid

        
        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0

        The vertical 1s in the 1st column is a valid answer
        Every 1 itself is a valid answer
        1 1
        1 1

        Every straight chain is a rectangle 1 1 1
        
        how do you differ the 2 rectangles in such a case - the vertical one of area 2, and horizontal of 3
        1
        1 1 1

        Further
        1
        1 1 1
        1 1 1
          1


        Just looking at horizontal slices
        max(rect) for rows i.e max nummber of consecutive 1s in the row
        row 0 - 1
        row 1 - 3
        row 2 - 5
        row 3 - 1

        Just looking at vertical slices
        max(rect) for cols
        col 0 - 4
        col 1 - 1
        col 2 - 3
        col 3 - 3
        col 4 - 2

        Saw the solution:

        Thinking row wise, you want to build a histogram using a row as a base
        (Monotonic stack part similar to Leetcode 84. Largest Rectangle in Histogram)

        Monotonic stack pattern is a very common LC hard pattern

        Suppose you update heights for a row, you then calculate the largest rectangle area in a histogram using a monotonic stack

        """
        if not matrix:
            return 0

        if len(matrix) == len(matrix[0]) == 1:
            return int(matrix[0][0])


        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        heights = [0] * cols

        def largestRectangleArea(heights):

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


        for row in range(rows):
            for col in range(cols):
                heights[col] = heights[col] + 1 if matrix[row][col] == "1" else 0
            print(heights)
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
                
        """Final note:
            Can be optimized further probably with dp)
        """
