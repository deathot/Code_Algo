class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_cnt, ans = -1, 0
        for d in divisors:
            cnt = sum(1 for x in nums if x % d == 0)
            if cnt > max_cnt or cnt == max_cnt and d < ans:
                max_cnt, ans = cnt, d
        return ans