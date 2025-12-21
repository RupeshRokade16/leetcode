import math
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        h represents the number of hours you have to eat all bananas
        
        You have to return k (eating rate) close to h

        Sorting the piles, and then deciding a rate of eating from a range
        of minimum of the pile to max of pile?

        Need to have a math function as the condition in this case
        Also the range means sorted, and then we can do a binary search
        to find the right middle value at which the math function becomes 
        valid

        Instead of a math function, you may want to select a value using
        binary search and then traverse the array to calculate the time 
        required at that rate of eating bananas

        1, 2, 3, 4 -> if mid val = 2, h = 6
                   -> if mid val = 1, h = 10
        Therefore h = 6 is correct (the cutoff is the last answer which stays below
        target in such cases)

        NOTE: you also do not need a range, you just need 2 endpts to start
        this binary search, hence saving memory

        Struggling with keeping track of the last closest answer under
        the target h

        NOTE: time_taken < h. means you have to decrease the rate of eating 
        (mid val),
        hence you discard right half

        I removed the time_taken == h because we want to find a min time, 

        so I rather look for time_taken <= h (the only condition for a valid
        solution)

        Next, I recompute against prev result, where I do
        min(res, mid val) [Correction - this isnt needed as res is bound to 
        increase
        or go out of bounds i.e beyond h in the next iteration]


        Unique things to remember:
        Search space goes from 1 to max(piles)
        if time_taken <= h:
            #Update res with the middle value
            #Update ptrs and proceed
        """
        def calc_time(k, piles):
            res = 0
            for pile in piles:
                time_for_pile = math.ceil(pile/k)
                res += time_for_pile
            return res

        res = float('inf')
        l, r = 1, max(piles) #min banana rate, max banana rate
        while l <= r:
            mid = (l + r)//2
            
            time_taken = calc_time(mid, piles)

            
            if time_taken <= h: #Decrease the rate of eating, to increase 
            #time_taken
                #Could be a valid solution, hence store
                #res = min(res, mid)
                res = mid
                r = mid - 1
                continue
            
            else:
                l = mid + 1
        
        return res

            
