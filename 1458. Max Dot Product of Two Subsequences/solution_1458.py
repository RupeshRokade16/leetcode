class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        Any zero in a list will just result in 0 for that particular dot product

        The subsequence arrays must be of same lengths

        2 conditions
            - if arr1[i] and arr[2] are both positive, then that is a valid candidate
            - if arr1[i] and arr[2] are both negative, then that is a valid candidate
            Anything else is an invalid candidate

        [3, -2] [2, -6, 7]

        Opt 1: take [3, -2] and [2, -6]
        dot product = 6 + 12 = 18
        Opt 2: [Take just 1 num]
        check positive max(nums1) and positive max(nums2) - 3 and 7 = 21
        as well as negative i.e min(nums1) and min(nums2) - -2 and -6 = 12

        nums1 = [2,1,-2,5], nums2 = [3,0,-6]

        Would popping the number 0 be an effective move? - NO


        At every step, we must carefully chose between
            Pairing, or skipping or stopping
        We can using dynamic programming to avoid recomputing overlapping subproblems
        dp(i, j) -> max dot product obtainable using subsequences from:
            nums1[i:]
            nums2[j:]

        j ->    1   2   3   4   ...
        i -|    1
                2       (i,j)
                3
                4
                ...

        At each i,j, we can 
            1) Pair and continue
                nums1[i] * nums2[j] + dp(i+1, j+1)
            2) Skip element from nums1
                dp(i+1, j)
            3) Skip element from nums2
                dp(i, j+1)
            4) Pair and stop
                nums1[i] * nums2[j]
        We take the max of all 4 options, each i, j is stored in a memo table, hence computed only once

        T: O(n * m)
        M: O(i * j)

        This was an LC hard

        """


        memo = {}

        def dp(i, j):
            #if OOB, return negative inf, hence not considered in max calculation
            if i == len(nums1) or j == len(nums2):
                return float("-inf")

            if (i, j) in memo:
                return memo[(i, j)]

            take = nums1[i] * nums2[j]

            res = max(
                #4 Steps

                #take i,j and move forward
                take + dp(i + 1, j + 1),

                #take i, j and stop
                take,

                #skip nums1[i]
                dp(i + 1, j),

                #skip nums2[j]
                dp(i, j + 1)
            )

            memo[(i, j)] = res

            return memo[(i, j)]

        return dp(0, 0)
