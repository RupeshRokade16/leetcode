class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        """
        We need to find the line y = res where the area of squares above the line is equal to area below the line

        The res line will tend towards the heavier of the 2 squares

        Can I keep consuming 2 squares such that I reach the result?

        That way I could make this problem solvable by continuously solving subproblems

        If there is overlap, we should be good to move the square right (since moving along x direction wont affect the answer)

        We keep a count of the total area and res (y point) -> Wont work as the next element can be very high and very large and we wont be able to identify how much to jump - We could possibly merge attached boxes,
        but we cant still traingulate a merged box with a y gap

        Read the hint: Binary search on the answer
        so we know the answer would lie anywhere from y = 0 to y = max(y + l)
        But the answer has to be accuracte till 5 decimal places

        For every y, we calculate the total sum of squares underneath it

        2 concerns I had
            1) How to go to decimal values? - (l+r/2 gives a good decimal value to begin with, repeating 60 times brings us closer to the solution)
            2) How to caclulate area beneath the curr iterations mid value
                - Look at the base problem
                    We need to identify how much of the area of the current square in consideration we need to take
                    
                    
        """
        
        low, high, total_area = float('inf'), float('-inf'), 0

        for x, y, l in squares:
            total_area += l*l
            low = min(low, y)
            high = max(high, y + l)

        target = total_area / 2.0

        for i in range(60):

            mid = (low + high) / 2.0

            curr_area = 0

            for _, y, l in squares:
                curr_y = max(0, min(l, mid-y))  # mid - y be less than l if there's a cut, else greater than l (case where the square is completely below). We take 0 if mid - y becomes less than 0 (i.e box completely above)
                curr_area += l*curr_y

            if curr_area < target:
                low = mid
            else:
                high = mid

        return mid
