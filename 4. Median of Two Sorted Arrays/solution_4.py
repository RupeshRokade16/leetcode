class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        """ m and n can be different sized. This affects the median.
        We could construct a merged array but that would take the time complexity to m+n
        [1,2,3] [6,7]
        Median means the middle value of the combined list
        Types of arrays:
        one array has all smaller nums than the other
        one array has spaced out nums where the other array can occupy and/or extend
        
        What is needed is finding the value which would be the m+nth value of the
        combined list

        [0,7,8,9,10] and
        [1,2,3,4,5,6] 
        
        3<8
        The left half of the smaller array = 0,7 


        I was intitially thinking to start by finding m/2th and n/2th value. 
        Compare and see 
        But instead
        I can find the middle value at smaller array. Evaluate that to be a part of
        my small arrays left partition (with middle at largest value in left partition)
        Then we can just take the remaining number of elements to make the combined half from the bigger array. (We place the ptr at largest value in left partition taken at that array)
        In both these cases we also have access to the respective starting element of the right parititions. These are useful to evaluate the condition which determines if we have the right ptrs
        Condition - Aleft <= Bright and Bleft <= Aright

        if Aleft >= Bright, then we need to take less elements from A, so recompute
        middle by discarding the right half of A and only finding middle from left half
        if Bleft >= Aright, then we need to more elements from A, so recomputing middle by including the right. 

        Note that since we automatically fill up the remaining values from larger array, we can comfortably binary search on smaller array

        The ptrs we make are prone to go out of bounds (either over or under), 
        (in cases where we are taking the entire smaller array, so we add edge cases to it)

        """

        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2     #We only need to reach till half of the elements

        #Binary search on smallest only
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2 #Basically mid
            j = half - i - 2 #Calling it j as its not necessarily always at mid, -2 since index is at 0

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j+1 < len(B) else float("infinity")

            #If partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                #Reduce elements from A, recompute mid
                r = i - 1
            else:
                l = i + 1



        #Brute Force
        # i, j = 0, 0
        # res = []
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] <= nums2[j]:
        #         res.append(nums1[i])
        #         i += 1
        #     else:
        #         res.append(nums2[j])
        #         j += 1
        # if i < len(nums1):
        #     res.extend(nums1[i:])
        # if j < len(nums2):
        #     res.extend(nums2[j:])

        # length = len(res)
        # if length%2==0:
        #     print(length, length%2)
        #     return (res[length//2 - 1] + res[length//2])/2
        # else:
        #     print(length, length%2)
        #     return res[length//2]