class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(rem):
            # Base cases
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            
            # If we already calculated this remaining amount, return it
            if rem in memo:
                return memo[rem]
            
            min_coins = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)
            
            # Save the result in memo before returning
            memo[rem] = min_coins
            return min_coins

        ans = dfs(amount)
        return ans if ans != float('inf') else -1