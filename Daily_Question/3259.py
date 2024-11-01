# now  in x, if (A(x+1) + A(x+2) < B(x+2)), need switch
class Solution:
    def maxEnergyBoost(self, a: List[int], b: List[int]) -> int:

        c = (a, b)
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            return max(dfs(i - 1, j), dfs(i - 2, j ^ 1)) + c[j][i]
        return max(dfs(len(a) - 1, 0), dfs(len(a) - 1, 1))
            
            