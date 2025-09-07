class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Chose hashset to remove repetitions of a num
        
        For this input -> 100,4,200,1,3,2
        We can say that 
        1,2,3,4       100      200
        make up 3 sequences
        And the we would needd to find the longest one

        But how to recognize a sequence? 
        The beginning and end values (hashset would come into use here)

        We can use 2 for loops, 1st to store all start of sequences
        and 2nd to compute the length of each sequence

        Code can be cleaned up by identifying start of sequences in the first loop
        calculating their longest sequence length and checking against a max

        """
        
        hashset = set(nums)
        longest = 0
        start_of_seq = []

        for num in nums:
            #Identify start of a unique sequence
            if num-1 not in hashset:
                start_of_seq.append(num)
        for num in start_of_seq:
            curr = num
            curr_len = 1
            longest = max(curr_len,longest)
            while curr+1 in hashset:
                curr_len += 1
                curr += 1
            longest = max(curr_len,longest)
        return longest
