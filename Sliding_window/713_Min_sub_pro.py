class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        prod = 1

        if k <= 1:
            return 0

        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1

        return ans
    
'''
Summarize:
    1. T: O(n), S: O(1)
    2. [l, r] == [l + 1,..., r]
'''
s = 0
nums = [1, 2, 3]
for right, x in enumerate(nums):
    s += x
    print(s)
    if s > 3:
        print("test")
    print("test1")

    
            

