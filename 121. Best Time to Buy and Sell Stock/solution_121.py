class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        i, j are initialized to 0th and 1st index
        if prices[i] < prices[j], compute against res, move j ahead
        else:
            move i ahead

            and if i matches j, move j ahead
        """

        i, j = 0, 1
        profit = 0

        while j < len(prices):
            if prices[i] < prices[j]:
                profit = max(profit, prices[j] - prices[i])
                j += 1
            else:
                i += 1     #can just match i to j, instead of incrementing,
                if i == j: #and incrememnt j outside of both the if and else
                           #blocks
                    j += 1
        return profit