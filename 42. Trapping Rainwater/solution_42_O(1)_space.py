_class Solution:
    def trap(self, height: List[int]) -> int:
        """
        when solving for O(1) memory,
        we move according to the left and rightmax. 
        So when leftmax < rightmax, 
            we incrememnt l ptr
        else
            we decrement r ptr
        This ensures we sweep across all pts while also ensuring that the smaller of the
        two heights is used for computing the water at curr position (meaning we are 
        doing min(leftMax,rightMax) just not explicitly)

        We are updating leftMax (and rightMax) first in the nested block so that we
        never write a -ve to our res. But we can always:
            1. compute using leftMax - height[l]
            2. Write to res after max(0, water)
            3. Update leftMax
        (rightMax in the opposite case)

        We need to do L <= R for the while loop as there comes this situation:
        ***********************
        Evaluating R when l and r are  4 4
        Left and right max =  3 3
        Computed water & added to res =  2 9
        ***********************

        which would fail. This happens because, during each if or else block, we move ptrs
        but the values at the new ptrs are only computed when the outer if/else block is
        satisfied. And our requirement is to scan through the entire array

        Better solution -
        However if you instead move using the heights at l and r ptrs, you skip the need
        to keep it l <= r


        Intuition                 First solution	                Second solution
      When water is computed	At current pointer before moving	At pointer after moving
Needs to evaluate when l == r?	✅ Yes—last cell still pending	  ❌ No—meeting means finished
        Loop condition	        while l <= r	                    while l < r
        """

        """
        #Moving using left and rightMax solution

        leftMax, rightMax = height[0], height[-1]
        l, r = 0, len(height) - 1

        res = 0

        #L and R ptrs scan through the entire array
        while l <= r:

            if leftMax < rightMax:
                print('Evaluating L when l and r are ', l, r)
                #For curr position - compute a left max first
                leftMax = max(leftMax, height[l])
                water = leftMax - height[l]
                if not (l == 0):
                    res += water
                #Update leftMax since left was moved
                print('Left and right max = ', leftMax, rightMax)
                print('Computed water & added to res = ', water, res)

                l += 1

            else:
                print('Evaluating R when l and r are ', l, r)
                rightMax= max(rightMax, height[r])
                water = rightMax - height[r]
                if not (r == len(height) - 1):
                    res += water
                print('Left and right max = ', leftMax, rightMax)
                print('Computed water & added to res = ', water, res)
                r -= 1

            print("***********************")
        return res
        """

        #Moving using l and r ptrs

        leftMax, rightMax = height[0], height[-1]
        l, r = 0, len(height) - 1

        res = 0

        while l < r:
            if height[l] < height[r]:
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                r -= 1
        return res
