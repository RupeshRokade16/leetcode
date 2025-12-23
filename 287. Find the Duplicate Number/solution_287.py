class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        If the duplicate integer only appeared one time (total twice), 
        then bitwise operators might help

        1, 2, 3, 2, 2

        Cant modify array and cant use extra space (only O(1))

        [1, n] is the range, can have multiple duplicates (Hence also cant 
        use sum of range - sum of array)

        What if we replace the input array nums with a ListNode(num)? 

        0th index -> num = 1
        1st index -> num = 2

        if another index -> num = 2, we break and return

        So in essence, we know where num should be placed in our desired array
        beforehand. arr[0] should always have element 1
        arr[1] should always have element 2

        Instead of swapping, we replace curr element with abs(curr val - correct value)

        Multiple ways of writing this solution:
            - Negative marking -> loop through every num, compute its correct idx
                                    idx = abs(num) - 1, mark the value there as -ve
            - Bit Manipulation -> (Only for number repeating twice)
                                  Every num from 1 to n-1 should appear exactly once,
                                  but one number appears twice.
                                  So for each bit position, we compare:
                                    How many times this bit is set among all nums in arr
                                    How many times this bit should be set among nums 1 to n-1
                                  If bit appears more times in the array than expected, that
                                  bit must belong to the duplicate number

                                  Combining all such bits gives us the duplicate
            - Fast & slow ptrs -> Treat array as LL, each idx pts to next idx
                                  given by its value. Since one num is duplicated
                                  it creates a cycle. First meet of slow and fast
                                  confirms a cycle, then start a new slow ptr from
                                  start, and move both slows. They meet at the 
                                  duplicate
        """

        """
        Negative Marking

        for i, num in enumerate(nums):
            #The num at current position should be present at num - 1 idx
            #So we check that idx, mark it negative.
            #If already negative, we return the number as it is the duplicate
            correct_idx = abs(num) - 1
            if nums[correct_idx] < 0: #if already -ve
                return abs(num)
            nums[correct_idx] *= -1 #-ve = flag of visited
        return -1
        """

        """
        Bit Manipulation
        for each bit position from 0 to 31
        n = len(nums)
        res = 0

        for b in range(32):  #32 bit integer
            x = y = 0
            mask = 1 << b
            for num in nums:
                if num & mask:
                    x += 1
            for num in range(1, n):
                if num & mask:
                    y += 1
            if x > y:
                res |= mask

        return res
        """
        
        """
        Cycle in LL (Fast and slow ptrs)
        """

        slow, fast = 0, 0
        
        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]] #similar to .next.next
            if slow == fast: break

        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: break

        return slow
