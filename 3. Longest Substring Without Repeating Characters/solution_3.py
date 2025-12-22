class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """Can use a map to store last occurence of a 
        number and then jump left ptr to that position, this removes
        the added complexity of removing from the set one by one, 
        however the time complexity stays the same"""

        if len(s) < 2:
            return len(s)

        res = 0
        longest = set()
        i, j = 0, 1
        longest.add(s[i]) 

        while j < len(s) and i < j:
            left, right = s[i], s[j]
            #Decision space - decide whether to take the curr
            if right in longest:
                #Remove from set
                longest.remove(left)
                i += 1
                if i == j:
                    longest.add(s[i])
                    j += 1
            if right not in longest and longest:
                #Add to set
                longest.add(right)
                j += 1
            res = max(res, len(longest))

        return res


        """
        Neetcode Solution
        longest = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in longest:
                longest.remove(s[l])
                l += 1
            longest.add(s[r])
            res = max(res, len(longest))
        return res
        """