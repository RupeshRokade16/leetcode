class MinStack:
    """
    Problem: How do I make sure the min is always a O(1) in events such that
    the main array is appending or popping

    Intuition: A secondary stack that can hold some values could help - but
    what kind of values?

    Maybe the secondary stack will hold values that are smaller than the last value
    added to the secondary stack
    [1, 2, 0]
    [1, 0]
    getmin -> 0
    pop -> [1, 2] and [1, 0]
    top -> [2]
    getMin -> will return 0 even if it no longer exists in the stack

    Better: At each entry, write down the minimum for that position
    Problem: I didnt consider the edge case where, after enough pops, 
    my stack becomes empty. At that time I my code kept track of self.min
    but it should've just compared against float('inf')

    How would I code this the next time?
    Can keep just one stack, and note the min during each entry into the
    stack.
    Each push operation would be first:
        1) Check if the stack is empty or not
            If empty:
                new value is the min
            If not empty:
                last pushed number's corresponding min should be compared with 
                the new value to push the new value and corresponding min
    """

    def __init__(self):
        self.memory = []

    def push(self, val: int) -> None:
        if self.memory:
            last_min = self.memory[-1][1]
            #Compute and store min
            self.memory.append((val, min(val, last_min)))
        else:
            self.memory.append((val, val))

    def pop(self) -> None:
        return self.memory.pop()

    def top(self) -> int:
        return self.memory[-1][0]

    def getMin(self) -> int:
        return self.memory[-1][1]