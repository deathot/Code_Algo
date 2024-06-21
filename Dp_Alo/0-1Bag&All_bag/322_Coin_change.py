'''
322. 零钱兑换

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

Tc:
Sc:

Summarize:
1.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache
        def dfs(i, c):
            if i < 0:
                return 0 if c == 0 else inf

            if coins[i] > c:
                return dfs(i - 1, c)

            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)
            
        ans = dfs(n - 1, amount)
        return ans if ans < inf else -1
