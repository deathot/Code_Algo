'''
1. must a subarray(contiguous array)
2. return minimal length of subarray
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        s = 0
        left = 0

        for right, x in enumerate(nums):
            s += x
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right-left + 1)

        return ans if ans <= n else 0
    
'''
Summarize:
    1. T: O(n), S: O(1)
'''