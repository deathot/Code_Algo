leetcode_162_峰值元素是指其值严格大于左右相邻值的元素。


时间复杂度:o(logn)
空间复杂度:o(1)

总结:
1.左开右开区间

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) //2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return right
        