class Solution:
    def climbStairs(self, n: int) -> int:
        """
        How many distinct ways can you climb 1 step: 1
        2 steps: 2
        3 steps: sum of last steps(2) and steps(1)
        4 steps: sum of last, steps(3) and steps(2)

        Recursive call is recomputing same answer, better to cache it

        n = 2, res = 2
        n = 1, res = 1
        """

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        second_last, last = 1, 2

        for i in range(n-3): #-2 for skipping the first 2, and -1 for index 0
            curr = second_last + last
            second_last = last
            last = curr
        
        return second_last + last
