class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        """
        Brute Force - Compute all possible substrings, run isPalindrome on it,
        return the one with the highest length
        I can cancel out substring which arent palindromic early on perhaps

        We check b, ba, bab, baba, babad
        Then we check a, ab, aba, abad
        Then we check b, ba, bad
        Then a, ad
        Then d

        Building all substring: n^2
        Checking all substrings are palindrome: n * n^2 = n^3
        
        We can start at the middle and expand outwards

        bababd
        We start at b, nothing to the left so length = 1
        we start at a, 1 to the left and 1 to right, so length = 3

        Makes the solution: O(n^2)

        This skips the palindrome of equal lengths (edge case)

        Reach Manacher's algorithm, it can be used to solve this in O(n) time
        Manacher's algo makes the even lengthened strings odd (and odd remain odd) and uses dp
        It is done by adding a delimiter like "#" before and after each char in the string
        cbbd 
        #c#b#b#d# - len = 9
        """
        
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd length
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            #even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
