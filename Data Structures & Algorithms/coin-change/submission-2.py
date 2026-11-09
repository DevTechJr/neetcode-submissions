class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        options = [amount+1] * (amount+1)

        options[0] = 0

        for value in range(1, amount+1):
            for c in coins:
                if value - c >= 0:
                    options[value] = min(options[value], 1 + options[value-c])
        
        return options[amount] if options[amount] != (amount+1) else -1