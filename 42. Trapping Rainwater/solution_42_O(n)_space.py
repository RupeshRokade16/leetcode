class Solution:
    def trap(self, height: List[int]) -> int:
        """
        fast and slow ptrs? where we also keep track of the closest left tower and closest right
        tower. So that whatever area we explore, we can compute the max water storable there
        When elevation to the right increases, we find a new water trappable space
        So we can start by scanning towards the right, left tower can be affixed. The moment we find the
        same or greater height, 
        its time to scan a new search space after computing the water in the current search space

        For ease of understanding, let's define the left tower and right tower as the edges of a 
        container which can hold water
        Also we can compute maximum trappable area as we move the r ptr every time (not valid as left
        can be super huge and right would never reach that height)

        Why my soln wont work? 
            I was assuming left to be smaller. What if we have a left tower of 5 to begin with? 
            [WAIT] That is still the max left. So this way of working is still valid

        We gotta compute the min(left_tower, right_tower) - h[i] at every position
        So we need max height at left and max height at right for every position. We can calculate
        this before hand

        What I missed? 
            The general formula for computing max water at each height is dependent on max to the left
            and max to the right of the search space. We then take the minimum of the two and subtract
            the height at curr position to get the units of water which we can store

            We would compute the max at left and max at right for each element before computing the
            trapped water at each element
            This is mainly what I lacked in my solution where I didnt know the bounds for each element

            Also, note that there are times where there would be negative totals at each element. We
            need to skip such answers as they actually cannot hold any water (or make the total 0)
        """
        max_left = []
        for i in range(len(height)):
            if i == 0:
                max_left.append(0)
            else:
                last_max = max_left[-1]
                max_left.append(max(last_max, height[i-1]))
        
        max_right = []
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                max_right.append(0)
            else:
                last_max = max_right[-1]
                max_right.append(max(last_max, height[i+1]))
        max_right = max_right[::-1]

        total = 0
        for i in range(len(height)):
            L, R = max_left[i], max_right[i]
            #print("minimum height at i = ", i, min(L,R))
            curr_total = min(L,R) - height[i]         #This can become negative, as h[i] can be bigger
            total += max(curr_total, 0)               #Discard such results
            print(i, curr_total, total)
        print(max_left, max_right)
        return total
