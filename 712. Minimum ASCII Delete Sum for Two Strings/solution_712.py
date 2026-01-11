class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Sum would include ascii of every deleted char

        To keep the sum low, we delete as few chars as possible (and if you need to select, we select the lowest ascii char, i.e alphabetical ordered char first)

        We have to make 2 strings equal when these chars are deleted

        aes     aet

        deeelt  eelt

        Cant sort coz the relative order of the strings matter

        delete      leet
            can remove de -   lete  leet
            can remove e  -   let   let [Now strings are equal]
            could've removed t but sum wouldve increased
            couldve removed l but sum wouldve increased

        sea     eat
        ^       ^       How to decide which one to skip right now?
                        - Might need sorting or some set to confidently 
         ^       ^
        we ask if s is in s2, if no, goes to s1Res, i += 1
                  e is in s1, if yes, s2 -= 1, ptr ahead

        char[i] if its in s2, reduce count in s1 or s2? 
        char[i] if not in s2, add to res, 


        Looked at the hint:
            Let dp(i, j) be the answer for inputs s1[i:], s2[j:]

        Questions I have:
            For base case
                - a, t, what do we return? Do we use a counter of both strings? 
                Thinking that using a counter would defeat the purpose of dp, since
                we are making decisions on smaller slices with knowledge of bigger
                slices
            What about base case 2
                where we have ete, t
                what should be the next slice?
                    te, []?

        Solution:
            Instead of focusing what to delete, focus on what chars to keep
            We need to find common subsequence of s1 and s2 whose total ASCII
            value is as large as possible

            Total ascii sum of chars in both strings - 2 * (Sum of ascii chars of the "best" (not necessarily longest) common subsquence) = answer

            This problem becomes a weighted Longest Common Subsequence problem
            Normal LCS - maximizes length
            This one - maximizes ascii value

            dp(i, j) -> maximum ascii sum of common subsequence between
                        - the first i chars in s1
                        - the first j chars in s2
                     -> What is the maximum ASCII value we can keep using prefixes
                        s1 upto i and s2 upto j

        Good solution at : https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solutions/7482930/you-dont-understand-youll-understand-now-k6jd

        See the image of your solution diagram
        """


        n, m = len(s1), len(s2)

        #dp[i][j] = max ascii sum of common subsequence
        dp = [[0] * (m + 1) for _ in range(n + 1)]  #padded matrix
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    #add it to your max ascii sum
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    #max of skipping s1[i-1] vs skipping s2[j-1]
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total_ascii - 2 * dp[n][m]
