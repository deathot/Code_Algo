class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rem = mean * (n + len(rolls)) - sum(rolls)
        if not n <= rem <= n * 6:
            return []
        avg, extra = divmod(rem, n)
        return [avg + 1] * extra + [avg] * (n - extra)