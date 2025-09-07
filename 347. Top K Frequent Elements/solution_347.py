class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        My traditional thinking approach - 
            create 2 hashmaps - 
                one that has nums -> count and then building
                one where count -> list of nums. 
            Next would be converting that count to a list and making sure I can 
            access the biggest count and backwards. Which makes it more complex.
            I didnt code till the solution though. What needcode did was use a 
            list of list to build the frequency array while preserving the order.

        What I was missing - 
            The first hashmap is necessary, the second hashmap doesnt store order which
            would make the solution go beyond O(n) time.
            Hence, instead of the second hashmap, we need to build an array holding arrays
            Specifically, an array whose indices would match the count we get from the hashmap we built
            At each index, we will store a list as there can be a random number of elements repeating
            at the count. 

        example - 
            nums = [1,2,2,2,3,3,3,3]

            We build countMap 
            countMap = {(1,1),(2,3),(3,4)}
            freq = [ [], [1], [], [2], [3]]
                idx   0   1   2    3    4 
        """

        countMap = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            countMap[num] += 1
        for num, cnt in countMap.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
                