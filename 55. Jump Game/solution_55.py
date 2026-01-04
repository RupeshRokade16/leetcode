class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Thinking I can traverse this array opposite, build a corresponding array which stores False
        
        Thought R to L
        at every point, if I can jump OOB or to the last index, I mark it true

        If I can hop to a true marked position, I mark that ith position (from where I would hop)
        as true as well

        I technically do not need to use extra memory, I can shift my goal post backwards

        """
        if len(nums) == 1:
            return True
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            
            jump = nums[i]

            if i + jump >= goal:
                goal = i
                continue
            
        return True if goal == 0 else False
            # hop = i + jump
            # while hop > i:
            #     if possible[hop] == True:
            #         possible[i] = True
            #     hop -= 1
        #return possible[0]
