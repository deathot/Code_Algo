class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * (len(nums) - k + 1)
        cnt = 0
        for i, x in enumerate(nums):
            cnt = cnt + 1 if i == 0 or x == nums[i - 1] + 1 else 1
            if cnt >= k:
                ans[i - k + 1] = x
        return ans
