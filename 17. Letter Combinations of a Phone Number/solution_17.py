class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Each element in the list a list of the options for the combination
        Each digit pressed == one of the three or 4 elements being picked

        from each list, you choose one number and pass it off to the next list

        Couldve used an array to build this off too

        T: O(n*4^n)
        """
        
        numToChar = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }


        res = []

        #i - for moving across the string

        def dfs(i, array):  #i will be curr position for the sublist

            if i >= len(digits):
                res.append("".join(array))
                return
            
            curr_number = digits[i]         #2 or 3
            curr_space = numToChar[curr_number]     #[a,b,c] or [d,e,f]

            for option in curr_space:
                array.append(option)
                dfs(i + 1, array)
                array.pop()            

        dfs(0, [])

        return res
