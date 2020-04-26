class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [[10000000 for _ in range(amount)] for _ in range(len(coins))]

        for i in range(len(coins)):
            for j in range(1, amount+ 1):
                if j % coins[i] == 0:
                    