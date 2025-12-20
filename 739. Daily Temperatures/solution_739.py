class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Thought process first is 
        What if I process each element and add it to a stack?
        What would the conditions be?
        temperatures = [30,38,30,36,35,40,28]
        How do I keep track of the number of days gone between 38 and 40?

        It is hard to justify why use a stack? (I read that when solving via
        Neetcode), but want to understand how to identify this

        At every element, we want to REMEMBER the previous elements
        So we can build a stack for all the previous elements (along w the index)
        which are unsolved, are then upon finding a valid high, keep popping till
        it works for the stack top

        The condition meaning when they are unsolved is when there is no higher 
        temp
        """
        res = [0] * len(temperatures)
        stack = [] #[(30,0), (38, 1)]
        for i, temp in enumerate(temperatures):
            if i == 0:
                stack.append((temp, i)) #tuple of temp and index
                continue
            if stack and temp > stack[-1][0]:
                #Keep popping till valid and compute to res
                while stack and stack[-1][0] < temp:
                    old_temp, old_idx = stack.pop()
                    res[old_idx] = i - old_idx
                    

            stack.append((temp, i))

        return res
            