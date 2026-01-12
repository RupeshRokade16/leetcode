class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Thought that I could calculate distance and floor but that's incorrect

        Move diagonally first and then move horizontally or vertically to cover the remaining distance

        Heuristic:
            for x1,y1 and x2,y2
            you are taking the max of abs(x1 - x2), abs(y1 - y2)
        """

        # x1, y1 = points[0]
        # res = 0
        # i = 1

        # while i < len(points):

        #     x2, y2 = points[i]

        #     diagonal = (0,0)
        #     if x1 < x2 and y1 < y2:
        #         diagonal = (1, 1)
        #     if x1 < x2 and y1 > y2:
        #         diagonal = (1, -1)
        #     if x1 > x2 and y1 < y2:
        #         diagonal = (-1, 1)
        #     if x1 > x2 and y1 > y2:
        #         diagonal = (-1, -1)

        #     while x1 != x2 and y1 != y2:
        #         #move diagonally according to where pt x2,y2 is relative to x1, y1
        #         x1 += diagonal[0] 
        #         y1 += diagonal[1]
        #         res += 1

        #     if x1 == x2:
        #         #add the diff of ys
        #         res += abs(y2 - y1)

        #     elif y1 == y2:
        #         #add the diff of x2
        #         res += abs(x2 - x1)

        #     i += 1
        #     x1, y1 = x2, y2
        
        # return res

        """
        Cleaner
        """
        x1, y1 = points[0]
        res = 0
        
        for i in range(1, len(points)):
            x2, y2 = points[i]

            res += max(
                abs(x1 - x2),
                abs(y1 - y2)
            )

            x1, y1 = x2, y2

        return res
