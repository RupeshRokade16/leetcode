class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        len(s1) < len(s2)

        abc                         abc
        ^
        lecabee                     lecaabee
           ^
        Brute force - computing permutations, then checking against s2
        But this requires memory

        abc
        ^
        cab
         ^ 
        We can establish that our search window will be of len(s1),
        when we find s1[0] in s2

        The search window can go back, can go front or anywhere in the middle

        If not found, we search for the next occurence of the char at s1[0]  

        Wrote a solution but with a lot of lines of code, 
        The idea was using a product of ascii representation of s1's characters
        Then defining search space when first char of s1 found in s2
        Do the same for all occurences of s1's first char in s2
        Then using each search space, check if the window of 
        searchSpaceptr - len(s1) to searchSpacePtr + len(s1) contains the ord
        product

        Following is the neetcode way which leverages the fact that the memory
        used will be O(26)
        """
        #Edge case
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26

        #Build s1 count, and init window of s2's count
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        #Check if both count arrays are a match, match = 26 is what we want
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            #Add s2[r] to the array
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            #Just lost the match by adding
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            #Remove s2[l] from array
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            #Just lost the match by reduction
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1
        return matches == 26
