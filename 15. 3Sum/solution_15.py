class Solution:
    """
    My thought process:
    We need a sorted list to avoid recounting already computed entries (duplicates)
    We loop over each number, and then establish a 2ptr based search window
    Stuck with 2 problems:
        What to do we repeating numbers? They are useful, but can be skipped sometimes. Here
        we can keep skip just the first number of the triplet
        How to increment ptrs correctly

    What I missed:
        After fixing the first number, the problem is essentially a 2 sum problem
        What I also wrongly considered was initializing slow and fast ptrs, instead of 
        initializing them at L and R
        If sum > 0, i'll update right
        if sum < 0, i'll update left
        if sum == 0, I'll store the ans and then update ptr while avoiding duplicates
            -all I need to do is update just 1 of the 2 ptrs

    T: O(nlogn) + O(n^2) = O(n^2)
    S: O(1) or O(n), depends on the sorting library

    Additional notes:
        This can be reduced to a Problem 167. Two Sum II type problem with the added twist
        of duplicates and non sorted input list 
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # [-4,-1,-1,0,1,2]

        #Select a number first and then establish a search window
        for idx, a in enumerate(nums):
            #edge case: search window not long enough
            if idx == len(nums) - 1:
                break

            #Do not compute if the num is +ve
            if a > 0: 
                break
            
            #Skip past duplicate number, since it is already computed. Avoid entering for idx = 0
            if idx > 0 and a == nums[idx - 1]:
                continue
            
            #Establish search window
            l, r = idx + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    #Would need to update ptrs here, since the window could be [-2, -2, 0, 0, 2, 2]
                    #and we would need to skip past duplicates. Skipping past duplicates on any 
                    #one side would be enough as the loop would take care of the other ptr
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    #As mentioned, you can update r too. Just comment out left then
                    #r -= 1
                    #while nums[r] == nums[r + 1] and l < r:
                    #    r -= 1
                    
        return res
