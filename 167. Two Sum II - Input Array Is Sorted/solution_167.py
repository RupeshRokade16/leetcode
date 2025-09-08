class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Since the array is sorted and we are guaranteed exactly one solution, we can 
        confidently use the two-pointer technique:
        - Start with one pointer at the beginning (smallest element) and one at the end 
        (largest).
        - If the sum is less than target, move the left pointer right (to increase sum).
        - If the sum is greater than target, move the right pointer left (to decrease sum).
        - Stop when the sum equals target.

        Without the guarantee of a solution, we couldn’t safely eliminate numbers this way. 
        We would instead need either:
            - Extra space (hash map/set) to check complements in O(1), or
            - Nested loops (O(n^2)) to exhaustively test all pairs.
        """
        left_idx, right_idx = 0, 0
        i,j = 0, len(numbers)-1

        while i<j:
            left_num, right_num = numbers[i], numbers[j]

            if left_num + right_num == target:
                left_idx, right_idx = i+1, j+1
                break
            if left_num + right_num > target:
                j -= 1
                continue
            if left_num + right_num < target:
                i += 1

        return [left_idx, right_idx]
