class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        m = nums[-1]
        f = [0] * (m + 1)
        for j in range(min(nums[0], m) + 1):
            f[j] = 1
        for pre, cur in pairwise(nums):
            j0 = max(cur - pre, 0)
            m2 = min(cur, m)
            if j0 > m2:
                return 0 
            for j in range(1, m2 - j0 + 1):
                f[j] = (f[j] + f[j - 1]) % MOD
            f[j0: m2 + 1] = f[:m2 - j0 + 1]
            f[:j0] = [0] * j0
        return sum(f) % MOD