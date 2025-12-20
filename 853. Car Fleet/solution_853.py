class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #distance = s * t
        """
        The car at the most forward position is a bottleneck
        That's a good start point for computing the first fleet

        Hence sort the positions in a desc order

        Then we calculate what time the front most car reaches the destination
        Then for the next car, if their time to destination is earlier the previous
        car, then they become a fleet with the previous car (i.e only keep prev car)
        else they are a separate fleet

        Since we want to keep the previous car fleet in mind (think top of stack)

        Only keep increasing values, delete all decreasing values 
        """

        arr = []
        hashmap = defaultdict(int) #posi -> speed, to save the speeds
        for i, posi in enumerate(position):
            hashmap[posi] = speed[i]

        position.sort(reverse=True)

        time_to_destination = [] #[3, 3, 5, 10] 

        for i, posi in enumerate(position):
            remaining = target - posi
            speed = hashmap[posi]
            time_to_finish = remaining / speed
            #time_to_destination[(time_to_finish, position)]

            if time_to_destination and time_to_destination[-1][0] >= time_to_finish:
                #Curr car becomes a fleet, so skip
                continue
            time_to_destination.append((time_to_finish, position))
            print(time_to_destination)

        return len(time_to_destination)

        """#Neetcode Solution

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []

        for p, s in pair:
            time_to_destination = (target - p) / s
            stack.append(time_to_destination)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
        """



