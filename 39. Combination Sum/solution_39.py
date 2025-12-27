class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        2 decisions, you choose a number or you do not choose

        [2,3,5], target = 8

        [] 

        [2]           (choose 2)

    [2,2] 

        Solution - First compute res, check OOB and then move and pass sum and new elements or remove and pass

        T: n*2^n (n because we are copying an array)
        """
        res = []

        def dfs(i, curr_sum, curr_arr):


            if curr_sum == target:
                #curr_arr is a valid answer, append
                res.append(curr_arr.copy())
                return
            
            if i >= len(candidates) or curr_sum > target:
                return

            #explore further
            curr_arr.append(candidates[i])
            dfs(i, curr_sum + candidates[i], curr_arr)

            curr_arr.pop()
            dfs(i + 1, curr_sum, curr_arr)

            # if curr_sum + candidates[i] < target:
            #     curr_arr.append(candidates[i])
            #     dfs(i, curr_sum + candidates[i], curr_arr)
            # else:
            #     curr_arr
            #     dfs(i + 1, curr_sum, curr_arr)

        dfs(0, 0, [])
        return res
