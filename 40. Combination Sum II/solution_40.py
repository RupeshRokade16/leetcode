class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        """
        To avoid duplicates, I will sort candidates first
        then skip past duplis

        Brute: I could also build solution like the previous question, loop through the res array and remove all entries (lists) with repeating integers

        Wont work because if candidates array has [2,5,2,1,2] we can choose these duplicates, but we can only choose a number once

        We need to pick a number of drop it and move to the next
        (but for the next iteration, we need to make sure not to include any numbers from iteration)

        We sort to help skip past duplicates
        At every decision point, we 
            1) Take the curr number, move to the next number, pop
            2) Skip index till curr number wont be decision space again (kinda like 3Sum)
        """
        # candidates = list(set(candidates))
        # print(candidates)
        candidates.sort()
        
        res = []

        def dfs(i, curr_sum, curr_arr):

            #check if we reached the target
            if curr_sum == target:
                res.append(curr_arr.copy())
                return

            #base case
            if i >= len(candidates) or curr_sum > target:
                #stop compute
                return

            #Append curr number and undo after recursive call
            curr_arr.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i], curr_arr) #i+1 will ensure next number selected
            curr_arr.pop()
            
            #Do not include next number (also skip past same ones)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i+1, curr_sum, curr_arr)

        dfs(0, 0, [])
        return res
