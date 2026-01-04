class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Can take 1 or 2 steps

        at each step, there's a cost associated to taking the next step (same cost even if I decide to take 1 step or 2)

        For array [10, 15, 20]

        To get to 2nd index (20),
        The 2 options are 10 and 15. Cheapest is 10
        To get to 3rd index (OOB),
        the 2 options are Cheapest(2nd index) + 2nd index val or Chepeast(1st index) + 1st index val

        """
        n = len(cost)
        total_steps = n + 1
        cheapest = 0
        last, second_last = 0, 0
        for i in range(2, n + 1):
            #cheapest at i = min(cheapest at prev + prev, cheapest at 2nd prev + 2nd prev)
            cheapest = min(last + cost[i - 1], second_last + cost[i - 2])
            second_last = last
            last = cheapest

        return cheapest
