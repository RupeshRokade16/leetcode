class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Initially think if keeping a dictionary makes sense,
        to keep a track of how many characters we have
        atleast to track a majority

        XYZAAAAA  k = 1
        X
        XY
        Z is the third number, so remove X and compute - YZ
        ZA
        ZAA
        ZAAA
        ZAAAA
        ZAAAAA

        The distinct numbers in the set can actually be given by len(set)
        but not the distinct number of each items repetition

        XYZZYAYAAAAA  k = 1

        {x}
        len(set) = 1, and y not in set allowed - {xy}
        len(set) = 2, z not in set - disallowed till set changes {y}
        {yz} - incrememnt r
        YZZ - {yz} - another Z allowed, increment r
        {yz} another Y allowed? it would've been if we had just one z

        So count of each element required 
        Still, how to keep a count of the majority element? 

        If we keep the left as the majority element
        Then 
        XYZZYAYAAAAA  k = 1
        X majority,
        Y can be added, room for error now 0
        Z cant be added as room for error = 0
        Keep Removing majority element, then room for error = 1
        YZ (Y majority element), room for error = 0
        Another Y cant be added, keep removing Y till room for error = 1
        ZZ (Z majority element), room for error = 1 
        
        WRONG, keeping left as majority element doesnt work as YZZ is a valid
        sequence which this algorithm will ignore

        So back to needing count of each element, and keeping track of 
        majority element during each add, remove operation

        Using window length - count[most_freq_char]
        CONDITION: WindowLength - count[most_freq_char] should be less than equal to k

        """

        countMap = defaultdict(int) #char -> freq

        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            countMap[s[r]] += 1
            maxf = max(maxf, countMap[s[r]])

            while (r - l + 1) - maxf > k:
                countMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res



